import jmespath

from typing import Any, Dict, Iterator
from requests import Session, Response
from loguru import logger
from typing import Optional
from datetime import datetime
from tiktokcomment.typing import Comments, Comment

class TiktokComment:
    BASE_URL: str = 'https://www.tiktok.com'
    API_URL: str = '%s/api' % BASE_URL

    def __init__(
        self: 'TiktokComment'
    ) -> None:
        self.__session: Session = Session()
    
    def __parse_comment(
        self: 'TiktokComment',
        data: Dict[str, Any]
    ) -> Comment:
        data: Dict[str, Any] = jmespath.search(
            """
            {
                comment_id: cid,
                username: user.unique_id,
                nickname: user.nickname,
                comment: text,
                create_time: create_time,
                avatar: user.avatar_thumb.url_list[0],
                total_reply: reply_comment_total
            }
            """ ,
            data
        )
    
        comment: Comment = Comment(
            **data,
            replies=list(
                self.get_all_replies(data.get('comment_id'))
            ) if data.get('total_reply') else []
        )

        logger.info('%s - %s : %s' % (
                comment.create_time,
                comment.username, 
                comment.comment
            )
        )

        return comment

    def get_all_replies(
        self: 'TiktokComment',
        comment_id: str
    ) -> Iterator[Comment]:
        page: int = 1
        while True:
            if(
                not (replies := self.get_replies(
                    comment_id=comment_id,
                    page=page
                ))
            ): break
            for reply in replies:
                yield reply
            
            page += 1

    def get_replies(
        self: 'TiktokComment',
        comment_id: str,
        size: Optional[int] = 50,
        page: Optional[int] = 1
    ):
        response: Response = self.__session.get(
            '%s/comment/list/reply/' % self.API_URL,
            params={
                'aid': 1988,
                'comment_id': comment_id,
                'item_id': self.aweme_id,
                'count': size,
                'cursor': (page - 1) * size
            }
        )

        return [
            self.__parse_comment(
                comment
            ) for comment in response.json().pop('comments')
        ]
    
    def get_all_comments(
        self: 'TiktokComment',
        aweme_id: str
    ) -> Comments:
        page: int = 1
        all_comments = []
        
        # Initial fetch to get video info
        initial_data = self.get_comments(aweme_id=aweme_id, page=1)
        if not initial_data or not initial_data.comments:
            return Comments(comments=[], caption=None, video_url=None, has_more=False)

        all_comments.extend(initial_data.comments)
        caption = initial_data.caption
        video_url = initial_data.video_url
        
        page = 2
        while True:
            logger.info(f"Fetching page {page} of comments...")
            comments_data = self.get_comments(aweme_id=aweme_id, page=page)
            if not comments_data or not comments_data.comments:
                logger.info("No more comments found.")
                break
            
            all_comments.extend(comments_data.comments)
            
            if not comments_data.has_more:
                logger.info("Last page of comments reached.")
                break
            
            page += 1

        return Comments(
            comments=all_comments,
            caption=caption,
            video_url=video_url,
            has_more=False  # All pages have been fetched
        )

    def get_comments(
        self: 'TiktokComment',
        aweme_id: str,
        size: Optional[int] = 50,
        page: Optional[int] = 1
    ) -> Comments:
        self.aweme_id: str = aweme_id

        response: Response = self.__session.get(
            '%s/comment/list/' % self.API_URL,
            params={
                'aid': 1988,
                'aweme_id': aweme_id,
                'count': size,
                'cursor': (page - 1) * size
            }
        )

        data: Dict[str, Any] = response.json()

        if not data or not data.get('comments'):
            return Comments(
                comments=[],
                caption=None,
                video_url=None,
                has_more=False
            )

        comments_data = data.pop('comments')
        return Comments(
            comments=[
                self.__parse_comment(
                    comment
                ) for comment in comments_data
            ],
            caption=comments_data[0].get('share_info', {}).get('title'),
            video_url=comments_data[0].get('share_info', {}).get('url'),
            has_more=data.get('has_more')
        )
    
    def __call__(
        self: 'TiktokComment',
        aweme_id: str
    ) -> Comments:
        return self.get_all_comments(
            aweme_id=aweme_id
        )
