import json
from didkit import key_to_verification_method, verify_presentation


async def verify_vp_credential(request):
    """Verifies a generated VP using
    SpruceID DIDKit

    Args:
        request (flask.Request): flask API request containing 
        the issued VP to be Verifiable

    Returns:
        Dict: DIDKit verification response in Python dict format
    """
    # Access the server-generated jwk key
    with open("key.jwk", "r") as f:
        key = f.readline()
    f.close()
    # Generate a verification method using the jwk key
    verification_method = await key_to_verification_method("key", key)
    # Generate the proof options so we can verify the VP
    didkit_options = {
        "proofPurpose": "assertionMethod",
        "verificationMethod": verification_method,
    }
    vp = request.form.get("input_vp")
    # Verify the presentation using SpruceID DIDKit library
    verifiable_vp = await verify_presentation(vp, json.dumps(didkit_options))
    return json.loads(verifiable_vp)
