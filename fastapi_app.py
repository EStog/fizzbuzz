from fastapi import Depends, FastAPI, Query
from starlette.responses import PlainTextResponse, StreamingResponse

from constants import (CLASSIC_FIZZBUZZ_PREFIX, N_ARGS_NAME, SEP_ARGS_NAME,
                       STREAM_PATH)
from fizzbuzz_lib import classic_fizzbuzz_as_gen_text, classic_fizzbuzz_as_text

app = FastAPI()

classic_fizzbuzz_tag = 'Classic FizzBuzz'


class ClassicFizzBuzzParams:
    def __init__(
        self,
        n: int = Query(..., description="The maximum number of the sequence",
                       alias=N_ARGS_NAME),
        sep: str = Query(' ', description="The separator of each element in the sequence",
                         alias=SEP_ARGS_NAME)
    ) -> None:
        self.n = n
        self.sep = sep


@app.get(f'/{CLASSIC_FIZZBUZZ_PREFIX}/', tags=[classic_fizzbuzz_tag], response_class=PlainTextResponse)
async def get_classic_fizzbuzz_as_text(params: ClassicFizzBuzzParams = Depends()):
    """Gives classic FizzBuzz result as a single plain text
    """
    return classic_fizzbuzz_as_text(params.n, params.sep)


@app.get(f'/{CLASSIC_FIZZBUZZ_PREFIX}/{STREAM_PATH}', tags=[classic_fizzbuzz_tag])
async def get_classic_fizzbuzz_as_stream(params: ClassicFizzBuzzParams = Depends()):
    """Gives classic FizzBuzz result as a stream
    """
    return StreamingResponse(classic_fizzbuzz_as_gen_text(params.n, params.sep),
                             media_type='text/plain')
