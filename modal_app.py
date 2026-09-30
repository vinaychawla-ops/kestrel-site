"""Serve the cleaned Kestrel static site on Modal.

Deploy:  MODAL_TOKEN_ID=... MODAL_TOKEN_SECRET=... modal deploy modal_app.py
"""

import modal

app = modal.App("kestrel-site")

image = (
    modal.Image.debian_slim()
    .pip_install("fastapi")
    # copy=True: bake files into the image so redeploys can never serve stale code
    .add_local_dir("kestrel-clean", remote_path="/www", copy=True)
)


@app.function(image=image)
@modal.asgi_app()
def web():
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    web_app = FastAPI()
    # html=True serves index.html at /
    web_app.mount("/", StaticFiles(directory="/www", html=True), name="static")
    return web_app
