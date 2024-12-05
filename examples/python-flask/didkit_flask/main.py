import errno
import json
import os
from socket import AF_INET, SOCK_DGRAM, socket

from didkit import generate_ed25519_key
from flask import Flask, jsonify, render_template, request
from flask_qrcode import QRcode

from didkit_flask.issue_credential import req_issue_vc
from didkit_flask.verify_credential import verify_vc_credential
from didkit_flask.issue_presentation import issue_vp_credential
from didkit_flask.verify_presentation import verify_vp_credential

app = Flask(__name__)
qrcode = QRcode(app)


@app.route("/")
def index():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()

    url = (
        (request.is_secure and "https://" or "http://")
        + IP
        + ":"
        + request.host.split(":")[-1]
        + "/wallet"
    )

    return render_template("index.html", url=url)


@app.route("/credential", methods=["GET", "POST"])
async def credential():
    credential = json.dumps(await req_issue_vc(request),
                            indent=2,
                            sort_keys=True)

    return render_template("credential.html", credential=credential)


@app.route("/wallet", methods=["GET", "POST"])
async def wallet():
    credential = await req_issue_vc(request)
    if request.method == "GET":
        return jsonify({"type": "CredentialOffer",
                        "credentialPreview": credential})
    elif request.method == "POST":
        return jsonify(credential)


@app.route("/issue_vc", methods=["GET"])
async def issue_vc():
    return render_template("issue_vc.html")


@app.route("/verify_vc", methods=["GET", "POST"])
async def verify_vc():
    if request.method == "GET":
        return render_template("verify_vc.html")
    elif request.method == "POST":
        validation = await verify_vc_credential(request)
        return jsonify(validation)


@app.route("/issue_vp", methods=["GET", "POST"])
async def issue_vp():
    if request.method == "GET":
        return render_template("issue_vp.html")
    elif request.method == "POST":
        presentation = await issue_vp_credential(request)
        return jsonify(presentation)


@app.route("/verify_vp", methods=["GET", "POST"])
async def verify_vp():
    if request.method == "GET":
        return render_template("verify_vp.html")
    elif request.method == "POST":
        presentation = await verify_vp_credential(request)
        return jsonify(presentation)


def main():
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        file_handle = os.open("key.jwk", flags)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    else:
        with os.fdopen(file_handle, "w") as file_obj:
            file_obj.write(generate_ed25519_key())
    app.run(host="0.0.0.0", port=5001)
