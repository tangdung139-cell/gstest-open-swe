# MailSenderService

## Description
This is a .NET 8 Console Application that provides a mail-sending service using SMTP. It reads configuration settings from `appsettings.json`, uses dependency injection, and logs operations.

## Setup Guide

### Prerequisites:
- Install .NET 8 SDK from [Microsoft's official website](https://dotnet.microsoft.com/download/).

### Steps to Set Up
1. Clone the repository:

```bash
git clone https://github.com/tangdung139-cell/gstest-open-swe.git
cd gstest-open-swe
```

2. Restore NuGet dependencies:

```bash
dotnet restore
```

3. Build the project:

```bash
dotnet build
```

4. Edit the `appsettings.json` file to provide your SMTP server configuration:

```json
{
  "Smtp": {
    "Host": "your_smtp_server",
    "Port": 587,
    "EnableSsl": true,
    "Username": "your_username",
    "Password": "your_password"
  }
}
```

5. Run the application:

```bash
dotnet run
```

The application will send a test email to `test@example.com` with a predefined subject and body.

### Logs
All logs are printed to the console. Ensure you have a terminal open to monitor the application's logging output.