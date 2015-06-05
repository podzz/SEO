from newspaper import Article, ArticleException


class ArticleParser:

    def get_corpus(self, article_url):
        article = Article(article_url, language='fr')
        article.download()
		try:
        	article.parse()
		except ArticleExcetion:
			return {}
        return {'title': article.title, 'authors': article.authors,
                'publish_date': article.publish_date, 'text': article.text,
                'image': article.top_image}
