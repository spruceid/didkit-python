# Flask Example

This project demonstrates use of verifiable credentials and presentation  for an
application.

## Dependencies

- Poetry ([installation instructions](https://python-poetry.org/docs/#installation))
- Python 3.7 or higher

### Python dependencies

```bash
$ poetry install
```

## Running

```bash
$ poetry run main
```

## Step-By-Step

First, open your browser on the selected host (default is http://localhost:5001)

<b>Note: This flask exemple creates a DID by default in key.jwk</b>

From there, you should see 4 options available:

1. Issue Verifiable Credential
2. Verify Verifiable Credential
3. Issue Verifiable Presentation
4. Verify Verifiable Presentation

### Issue a Verifiable Credential (VC)
The first step should be to generate a Verifiable Credential. To understand better 
what a VC is, please refer to SpruceID Glossary [here](https://www.spruceid.dev/references/glossary#verifiable-credentials-vcs)

In order to simplify this example, there are only 2 ways to issue a VC:

1. Read a QRcode via Credible
2. Get server issued credential

On a real case scenario, a unsigned credential would be required so DIDKit can sign it.
One can refer to this in the quickstart example [here](https://www.spruceid.dev/quickstart)

The issued VC will be presented in JSON format. Store this value for later use.

### Verify a Verifiable Credential (VC)
After successfully issuing a VC, the next step should be to verify it.

Copy and paste the issued VC from the first step and click on the button to verify it.
The default response should be:
```json
{
    "checks":["proof"],
    "errors":[],
    "warnings":[]
}
```
This means the given VC is valid.

### Issue a Verifiable Presentation (VP)
Now, one can use the valid VC to generate a Verifiable Presentation. To understand better
what a VP is, please refer to W3C exemple [here](https://www.w3.org/TR/vc-data-model-2.0/#dfn-verifiable-presentation)

<b>Note: in very brief terms, a VP can contain cherry-picked information from the original VC
in order to preserve sensitive/unwanted verifiable information </b>

To generate a VP using DIDKit, 3 variables are needed:
1. The unsigned VP
2. A valid VC
3. The VC holder identifier (in this example, a DID:key)

One can refer to this in the CLI example [here](https://www.spruceid.dev/didkit/didkit-examples/core-functions-cli#create-a-verifiable-presentation-that-embeds-the-verifiable-credential)

The default response should be:
```json
{
    "checks":["proof"],
    "errors":[],
    "warnings":[]
}
```
This means the given VP is valid.
