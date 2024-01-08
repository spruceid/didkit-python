import json
from didkit import verify_credential, key_to_verification_method


async def verify_vc_credential(request):
    """Verifies a generated VC using
    SpruceID DIDKit

    Args:
        request (flask.Request): flask API request containing 
        the issued VC to be Verifiable

    Returns:
        Dict: DIDKit verification response in Python dict format
    """
    # Access the server-generated jwk key
    with open("key.jwk", "r") as f:
        key = f.readline()
    f.close()
    # Generate a verification method using the jwk key
    verification_method = await key_to_verification_method("key", key)
    # Generate the proof options so we can verify the VC
    didkit_options = {
        "proofPurpose": "assertionMethod",
        "verificationMethod": verification_method,
    }
    # Verify the credential using SpruceID DIDKit library
    credential = await verify_credential(request.form.get('input_credential'),
                                         json.dumps(didkit_options))
    return json.loads(credential)
