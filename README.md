# MLX ParaLLM UI
A minimal UI for parallel inferencing based on https://github.com/willccbb/mlx_parallm.

![image](https://github.com/do-me/mlx_parallm_ui/assets/47481567/6d43145c-5922-4332-944c-91de7cd684ff)

## Installation 

1. Follow the setup instructions in https://github.com/willccbb/mlx_parallm, best install dependencies in a virtual env
2. Copy the files from this repo into `mlx_parallm` (main dir) 
3. `pip install fastapi==0.95.1 pydantic==1.10.4 starlette==0.27.0 uvicorn==0.22.0` to install missing dependencies
4. Run the fastapi server with `python fastapi_server.py` and open localhost:8000 in your browser

Inferencing for the first time downloads the model once to your computer.

## Idea 
Keep it super simple to set up. Using tailwind css and marked js dependencies from a cdn. 
As soon as mlx_parallm becomes a pip package, installation will become easier.

## Notes 
Note that MLX is specific for Apple Silicon, so you can only run it on the M-series of Macs. Tested on a Mac M3 Max 128Gb.
