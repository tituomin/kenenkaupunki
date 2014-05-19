# default 30 days
MAX_AGE = 2592000

class MaxAgeMiddleware(object):
    def process_response(self, request, response):
        response['Cache-Control'] = 'max-age={0},s-maxage:{0}'.format(MAX_AGE)
        return response
