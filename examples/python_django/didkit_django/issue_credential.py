from python_django.settings import KEY_PATH
from datetime import datetime, timedelta
import didkit
import json
import uuid


async def issueCredential(request):
    with open(KEY_PATH, "r") as f:
        key = f.readline()

    did_key = request.POST.get('subject_id', didkit.key_to_did("key", key))
    verification_method = await didkit.key_to_verification_method("key", key)
    issuance_date = datetime.utcnow().replace(microsecond=0)
    expiration_date = issuance_date + timedelta(weeks=24)

    credential = {
        "id": "urn:uuid:" + str(uuid.uuid4()),
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            "https://www.w3.org/2018/credentials/examples/v1",
        ],
        "type": ["VerifiableCredential"],
        "issuer": did_key,
        "issuanceDate": issuance_date.isoformat() + "Z",
        "expirationDate": expiration_date.isoformat() + "Z",
        "credentialSubject": {
            "@context": [
                {
                    "username": "https://schema.org/Text"
                }
            ],
            "id": "urn:uuid:" + str(uuid.uuid4()),
            "username": "Someone",
        },
    }

    didkit_options = {
        "proofPurpose": "assertionMethod",
        "verificationMethod": verification_method,
    }

    credential = await didkit.issue_credential(
        json.dumps(credential),
        json.dumps(didkit_options),
        key)
    return json.loads(credential)
