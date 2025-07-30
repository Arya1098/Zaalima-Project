import imaplib
import email
import os

SAVE_DIR = "./invoices"
os.makedirs(SAVE_DIR, exist_ok=True)

def fetch_latest_invoice(email_user, email_pass):
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_user, email_pass)
        imap.select("inbox")

        status, messages = imap.search(None, 'ALL')
        email_ids = messages[0].split()
        latest_email_id = email_ids[-1]

        status, msg_data = imap.fetch(latest_email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") and "attachment" in part.get("Content-Disposition"):
                filename = part.get_filename()
                if filename and filename.endswith(".pdf"):
                    filepath = os.path.join(SAVE_DIR, filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    return f"Invoice saved: {filename}"

        return "No PDF attachment found in latest email."
    except imaplib.IMAP4.error:
        return "Login failed. Check credentials."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        try:
            imap.logout()
        except:
            pass
