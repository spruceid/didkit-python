
from didkit import issue_presentation, key_to_verification_method
import json


async def issue_vp_credential(request):
    """Issue a VP credential using SpruceID DIDKit

    Args:
        request (flask.Request): Flask API request containing:
        Unsigned VP,
        Signed VC,
        Holder info

    Returns:
        Dict: Python dict containing a valid DIDKit VP
    """
    with open("key.jwk", "r") as f:
        key = f.readline()
    f.close()
    verification_method = await key_to_verification_method("key", key)
    didkit_options = {
        "proofPurpose": "assertionMethod",
        "verificationMethod": verification_method,
    }
    vp = json.loads(request.form.get("input_vp"))
    vc = json.loads(request.form.get("input_vc"))
    holder = request.form.get("holder")

    vp["verifiableCredential"] = vc
    vp["holder"] = holder

    presentation = await issue_presentation(json.dumps(vp),
                                            json.dumps(didkit_options), key)
    return json.loads(presentation)
