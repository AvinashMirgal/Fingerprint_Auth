# Fingerprint Authentication for payment withdrawal
In this Project there is 2 Main Module:
## 1) Admin panel  
## 2) User Login
We use Morpho Biometric device for fingerprint authentication and for Two Factor authentication we use OTP Validation.

# Admin Panel 
In this we first Register user Details like:
1) User Name
2) Mobile Number(for later 2 step authentication)
3) User initial balance
4) fingerprint registration

# User Login
In this form user enter there **Username and Mobile Number**
- After entering details User ask to enter **OTP** that is send on there Register Mobile Number
- After entering **OTP** User gets an Notification  ask to verify there fingerprint Using Morpho Biometric Device
- After Sucessfully verify there identity user go to the **User Amount Withdraw form** 
- In that user can enter the amount that is need to be withdraw from there respective account and after that window is close.
