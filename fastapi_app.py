from starlette.responses import PlainTextResponse, StreamingResponse
from fizzbuzz_lib import classic_fizzbuzz_as_gen_text, classic_fizzbuzz_as_text
from fastapi import FastAPI, Query, Depends

app = FastAPI()

classic_fizzbuzz_tag = 'Classic FizzBuzz'
classic_fizzbuzz_prefix = 'classic-fizzbuzz'

class ClassicFizzBuzzParams:
    def __init__(
        self,
        n: int = Query(..., description="The maximum number of the sequence"),
        sep: str = Query(' ', description="The separator of each element in the sequence")
    ) -> None:
        self.n = n
        self.sep = sep


@app.get(f'/{classic_fizzbuzz_prefix}/', tags=[classic_fizzbuzz_tag], response_class=PlainTextResponse)
async def get_classic_fizzbuzz_as_text(params: ClassicFizzBuzzParams = Depends()):
    """Gives classic FizzBuzz result as a single plain text
    """
    return classic_fizzbuzz_as_text(params.n, params.sep)


@app.get(f'/{classic_fizzbuzz_prefix}/stream/', tags=[classic_fizzbuzz_tag])
async def get_classic_fizzbuzz_as_stream(params: ClassicFizzBuzzParams = Depends()):
    """Gives classic FizzBuzz result as a stream
    """
    return StreamingResponse(classic_fizzbuzz_as_gen_text(params.n, params.sep),
                             media_type='text/plain')
