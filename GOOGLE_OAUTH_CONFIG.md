# 🔧 IMPORTANT: Google Cloud Console Configuration

##currently not working..... -> Soon updating

## ⚠️ CRITICAL STEP - Configure Redirect URIs

For Google OAuth2 to work, you MUST add these redirect URIs in your Google Cloud Console:

### Go to Google Cloud Console:
1. Visit: https://console.cloud.google.com/
2. Select your project
3. Go to: **APIs & Services** → **Credentials**
4. Click on your OAuth 2.0 Client ID
5. Scroll to **Authorized redirect URIs**

### Add ALL of these URIs:

```
https://127.0.0.1:8000/social-auth/complete/google-oauth2/
https://localhost:8000/social-auth/complete/google-oauth2/
https://mysite.com:8000/social-auth/complete/google-oauth2/
https://0.0.0.0:8000/social-auth/complete/google-oauth2/
```


#currently it is not working...

### Also add Authorized JavaScript origins:

```
https://127.0.0.1:8000
https://localhost:8000
https://mysite.com:8000
https://0.0.0.0:8000
```

### Save the configuration

Click **SAVE** at the bottom of the page.

---

## 🧪 Test Your Setup

### 1. Open your browser and go to:
```
https://127.0.0.1:8000/account/login/
```

### 2. Accept the certificate warning:
- Click "Advanced"
- Click "Proceed to 127.0.0.1 (unsafe)" or "Accept Risk"

### 3. You should see:
- Login form with username/password fields
- **"Sign in with Google"** button

### 4. Click "Sign in with Google"
- You'll be redirected to Google's login page
- Select your Google account
- Click "Allow" to grant permissions
- You'll be redirected back to your site's dashboard

---

## ✅ Success Indicators

If everything works correctly:
- ✅ No "redirect_uri_mismatch" error
- ✅ You're redirected to Google login
- ✅ After authorization, you're back on your site
- ✅ You're automatically logged in
-  You can see your dashboard at `/account/`

---

## 🐛 If You See Errors

### Error: "redirect_uri_mismatch"
**Cause**: The redirect URI doesn't match what's configured in Google Console
**Fix**: Double-check that you added ALL the redirect URIs listed above

### Error: "Access blocked: This app's request is invalid"
**Cause**: OAuth consent screen not configured properly
**Fix**:
1. Go to: **APIs & Services** → **OAuth consent screen**
2. Click "EDIT APP"
3. Fill in all required fields
4. Add your email as a test user
5. Save

### Error: "Invalid HTTP_HOST header"
**Status**:  FIXED - Added '0.0.0.0' to ALLOWED_HOSTS

---

## 📝 Your Current Configuration

**Client ID**: Stored in `.env` file as `GOOGLE_OAUTH2_KEY`
**Client Secret**: Stored in `.env` file as `GOOGLE_OAUTH2_SECRET`

**Server Running**: `https://0.0.0.0:8000/`
**HTTPS**: ✅ Enabled with cert.crt
**ALLOWED_HOSTS**: ✅ ['mysite.com', 'localhost', '127.0.0.1', '0.0.0.0']

---

##  Ready to Test!

Your server is running and configured. Now:
1. Add the redirect URIs to Google Cloud Console (see above)
2. Open https://127.0.0.1:8000/account/login/
3. Click "Sign in with Google"
4. Enjoy your working social authentication! 
