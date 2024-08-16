import pytesseract
import subprocess
import io
import webbrowser
import tempfile
from PIL import Image

def main ():
  process = subprocess.Popen(["flameshot", "gui", "--raw"], stdout=subprocess.PIPE)
  stdout, _ = process.communicate()
  image_stream = io.BytesIO(stdout)
  image = Image.open(image_stream)
  text = pytesseract.image_to_string(image, lang="jpn")
  html_content = f"<p>{text}</p>"
  tempf_path = None
  with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tempf:
    tempf.write(html_content.encode("utf-8"))
    tempf.flush()
    tempf_path = tempf.name
  webbrowser.open(f"file://{tempf_path}")
main()
