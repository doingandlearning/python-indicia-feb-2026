Below is a step-by-step guide you can follow. Take your time — just work through it in order.

---

# Fixing `pip install` Behind a Work Proxy (Windows)

You are seeing an error about a malformed or missing proxy. This usually means Python is trying to use your company’s proxy but doesn’t know the correct address.

We’ll fix it step by step.

---

## Step 1 — Make sure the command is correct

In your virtual environment, run:

```powershell
python -m pip install pytest
```

If it still fails with a proxy error, continue below.

---

## Step 2 — Find your company proxy address

1. Press the **Windows key**
2. Type **Proxy settings**
3. Open **Proxy settings**
4. Scroll to **Manual proxy setup**

If it is turned **On**, you will see:

- **Address**
- **Port**

You need both values.

Example:

- Address: `proxy.company.com`
- Port: `8080`

If you do not see an address or it looks incomplete, let Kevin know.

---

## Step 3 — Try installing using the proxy

In PowerShell, type this (replace with your real values):

```powershell
$proxy="http://proxy.company.com:8080"
python -m pip install --proxy $proxy pytest
```

Replace:

- `proxy.company.com` with your proxy address
- `8080` with your proxy port

If it works — great. You’re done.

If it fails, continue.

---

## Step 4 — Try again with trusted hosts

Some company networks inspect HTTPS traffic. Try this version:

```powershell
$proxy="http://proxy.company.com:8080"
python -m pip install --proxy $proxy --trusted-host pypi.org --trusted-host files.pythonhosted.org pytest
```

If it works — great.

If not, continue.

---

## Step 5 — Save the proxy permanently (so you don’t retype it)

1. In PowerShell, run:

```powershell
notepad $env:APPDATA\pip\pip.ini
```

2. If asked to create the file, click **Yes**

3. Paste this inside (replace with your proxy details):

```ini
[global]
proxy = http://proxy.company.com:8080
trusted-host =
    pypi.org
    files.pythonhosted.org
```

4. Save and close Notepad

5. Try again:

```powershell
python -m pip install pytest
```

---

## Step 6 — If nothing works

Run these three commands and send the output to Kevin:

```powershell
gci env:*proxy*
netsh winhttp show proxy
python -m pip install -v pytest
```

Do not worry about understanding the output — just copy and send it.

---

## Alternative (if proxy blocks everything)

If the company network completely blocks pip:

Kevin can download the required files and give them to you.

Then you would run:

```powershell
python -m pip install --no-index --find-links . pytest
```

This installs without using the internet.

---
