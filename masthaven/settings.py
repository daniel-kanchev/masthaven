BOT_NAME = 'masthaven'
SPIDER_MODULES = ['masthaven.spiders']
NEWSPIDER_MODULE = 'masthaven.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
    'masthaven.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
# LOG_LEVEL = 'DEBUG'
