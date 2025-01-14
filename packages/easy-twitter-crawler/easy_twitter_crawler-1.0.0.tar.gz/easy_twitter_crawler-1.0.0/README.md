# easy_twitter_crawler

推特（Twitter）采集程序，支持用户，发文，评论采集，希望能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

## 安装

```shell
pip install easy_twitter_crawler
```

## 主要功能

- `search_crawler` 关键词搜索采集（支持热门,用户,最新,视频,照片;支持条件过滤）
- `user_crawler` 用户采集（支持用户信息,用户发文,用户回复）
- `common_crawler` 通用采集（支持发文,评论）

## 简单使用

设置代理及cookie

```python
proxy = {
    'http': 'http://127.0.0.1:10808',
    'https': 'http://127.0.0.1:10808'
}
cookie = 'auth_token=686fa28f49400698820d0a3c344c51e3e44af73a; ct0=5bed99b7faad9dcc742eda564ddbcf37777f8794abd6d4d736919234440be2172da1e9a9fc48bb068db1951d1748ba5467db2bc3e768f122794265da0a9fa6135b4ef40763e7fd91f730d0bb1298136b'
```

关键词采集使用案例（对关键词指定条件采集10条数据）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, search_crawler, TwitterFilter

key_word = 'elonmusk'

twitter_filter = TwitterFilter(key_word)
twitter_filter.word_category(lang='en')
twitter_filter.account_category(filter_from='', to='', at='')
twitter_filter.filter_category(only_replies=None, only_links=None, exclude_replies=None, exclude_links=None)
twitter_filter.interact_category(min_replies='', min_faves='', min_retweets='')
twitter_filter.date_category(since='', until='')
key_word = twitter_filter.filter_join()

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in search_crawler(
        key_word,
        data_type='Top',
        count=10,
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

用户信息采集使用案例（采集该用户信息及10条文章，10条回复，10个粉丝信息，10个关注信息）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, user_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in user_crawler(
        'elonmusk',
        article_count=10,
        reply_count=10,
        following_count=10,
        followers_count=10,
        # start_time='2023-07-20 00:00:00',
        # end_time='2023-07-27 00:00:00',
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
    print(f"文章数：{len(info.get('article', []))}")
    print(f"粉丝数：{len(info.get('followers', []))}")
    print(f"关注数：{len(info.get('following', []))}")
    print(f"回复数：{len(info.get('reply', []))}")
```

通用采集使用案例（已知文章id，采集此文章信息）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, common_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in common_crawler(
        '1684447438864785409',
        data_type='article',
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

通用采集使用案例（已知文章id，采集此文章下10条评论）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, common_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in common_crawler(
        '1684447438864785409',
        data_type='comment',
        comment_count=10,
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

## 链接

Github：https://github.com/hanxinkong/easy_twitter_crawler

在线文档：https://easy_twitter_crawler.xink.top/

## 贡献者
