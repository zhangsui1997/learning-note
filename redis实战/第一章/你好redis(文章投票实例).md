## 用redis构建一个文章投票网站的后端。 ##  
使用两个有序集合来表示文章，第一个成员是文章ID，分值是发布时间。第二个成员是文章ID，分值是票数或者评分。 
为了防止重复投票需要为每一篇文章维护一个集合存储为他投票的用户ID。  
**使用 " : " 来分割数据结构的名字不同部分，比如文章散列:**
```
article_name:article_id:{
  title : XXX,
  time  : 124123.445,
  votes : 998
}
```

```
one_week_seconds = 7 * 24 * 60 *60
vote_score = 432 

def article_vote(conn,user,article):
	cutoff = time.time() - one_week_seconds
	#判断是否是一周前的文章
	if conn.zscore('time:',article) < cutoff:
		return 
	
	article_id = article.partition(':')[-1]
	if conn.sadd('voted:'+article_id,vote_score): # 添加用户到 voted:文章id 集合里
		conn.zincrby('score:', article , vote_score) # 自增:向 score: 有序集合中为相应的文章加分数
		conn.hincrvy(article, 'vote' ,1) # 自增:为这个文章散列的vote投票数加1   

```

