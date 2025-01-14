# chatlib.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Place your JSON Firebase config below
firebase_config = '''
{
  "type": "service_account",
  "project_id": "animomik-20f94",
  "private_key_id": "0ed66a609acec33739497f5c1dd324aedd64ec94",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQrT512q8NtccO\nS/PZViM1wcA6iY49fZmpwTGQ2qsP/StX0p4fAS2i2YzwFBr4mbZ+/ct9OiyynPlP\naYym2CQYAbhqjoopz+itUe+ym7Rio1FobtI2ENY4Fch5FsCBkQXk5PjcyvuX/dbk\nz0bpZmtauOhOa+/ysvjlXpKdXGx3eabKqz1DUXazSYF9X7ptUFh/cVUP4zERZhZN\nL4jLGp3Wh2besKhBlfq8Bow4I7lA8TT7gDWiECKRS+OZp4HKw+yWjULb3eYdKors\npnP5VnSrPpMaR6y9hV2po//qSLlKCSoB7Ncfx5ASCNmT8pWXhEM8MTWITKUKKSik\n4VxT506dAgMBAAECggEAMRq/UrDb1hRTK8pULq2uGemGoE+7tL0QUomnbgCC1f+b\nei5R7pZSpJpgZ6M3iI31S5NR1d1BZON66ES8aAt/DNYkzRBPM1EdHeHkz4kDzN1F\nHBfN6BKUsjxwAQyJTsPvWOJHrH8obqb5MT0UYPpsozvVUJTmMRyL5L+ZLSXxUTiW\nTN9Bft4vGyJIuzluC4PLUTlDPDjX/ETmQld2ausIXLsA23IP09emutKr6yJgpJUw\nxHnrUrf1GPZNegausCgFcvChEHXZXdL4bE33n7RZF8J6iJ9dpM03PAEdl6ic9UXZ\nVpmLEJ4xhrMkdbgr6aVhro5erBPmQUqPdduBrTTCAQKBgQD7chm/vFXwie5oYoCE\nvJWTERx0Wb/OnD2hIhsbqoQCwVaX3hVrOq/69wKd4iDK1Xt0IzzoBGDccit6ju9U\nk6qQ4DWpGfeIPWLTPcMzdKE2aOY/ukMwz5OpldlonWjwVc+ubBhbyvm667KMGNv2\nVHCOydZ06xUq3wq+R0Tg3xSCAQKBgQDUdNU6guRNG0B7eMzJok6RPZFjrUj1kYqr\ntA8KGSXxCXksr1fAQEF1mblwXuETR9OrfpdTuxH3u+CUmDohOXYIryhC/gOJIGTZ\nLnBytadByOxzR0kIgvKNtyIPAILU65iFCR9mD1drM9R/MQzs8cYfsQwkztuMsNe2\nUvzj0yuUnQKBgF7kn70RealulI/GZNQzS4uWEJQEbvOtWUDfWzWks29KwcBMqu6t\n1k4zPESTW2bRDGc3CTxSsq9fUvNM0BuuItfMFdQ8nYNID2zDSVC4+kJLcmGojMT2\nAbcle0gU586Tw+4Ck2rI/lhBrT9b/l9HXLc2iv3S3kkwpaBLyz3GUroBAoGAI6CL\n+Unl2wBM6eex/8YWAskeTmbKq1OCu5RwSTM6Z5c9GL82qeickYn7zNo8SC1tU37h\nBYuDUdXRrVlxtgyavI4S5FkQYrhp8PmWpcXMjH2TGSnFF4ZOAnHJZlahme8AHp8P\nAuBjunhwk/u3vSw2Gy5naOy/aHJnWg3ElrfcwQkCgYADfn2MsaVCGW1V6FzY4eci\n3KXuU2D+VJF1yZ2ZDBwsHirt0I6Mw9HXTrlELjbeYh3JRHzhBUtGC87SQ2G4bv4C\nw7PeFuYyYI7kcRkQIMaErLoSYGbzCrl593M0N7pIdVGlqlZ/qo4qpzQ0fV7Yhp3Q\nxfCUxcg9i1qUotoS58kKZA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-qdx53@animomik-20f94.iam.gserviceaccount.com",
  "client_id": "100211968033591147464",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qdx53%40animomik-20f94.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
'''

# Initialize Firebase
cred = credentials.Certificate(json.loads(firebase_config))
firebase_admin.initialize_app(cred)

db = firestore.client()

def read_messages():
    messages_ref = db.collection(u'messages')
    docs = messages_ref.stream()

    messages = []
    for doc in docs:
        messages.append(doc.to_dict())

    return messages

def write_message(alias, message_text):
    messages_ref = db.collection(u'messages')
    messages_ref.add({
        u'alias': alias,
        u'text': message_text,
        u'timestamp': firestore.SERVER_TIMESTAMP,
    })
