import os

import aiofiles
from sanic import Sanic
from sanic.response import text


ENV_FILE_ROOT = 'ML_FILE_ROOT'
ML_FILE_ROOT = os.getenv(ENV_FILE_ROOT, None)
if not ML_FILE_ROOT:
    raise EnvironmentError(
        'There is no ml file path. '
        'Please, provide {} environment variable'.format(ENV_FILE_ROOT))
app = Sanic()


@app.route('/<word:.+>/')
async def test(request, word):
    async with aiofiles.open(ML_FILE_ROOT) as f:
        async for line in f:
            if line.startswith(word):
                return text(line)
    return text('Not found', status=404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
