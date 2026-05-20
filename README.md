# MailSenderService

This is a .NET 8 console application that demonstrates how to send emails using an SMTP server with dependency injection, configuration, and logging.

## Prerequisites

- .NET 8 SDK
- An SMTP server for testing (e.g., Gmail SMTP, Mailtrap, etc.)

## Steps to Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gstest-open-swe/MailSenderService
   ```

2. Update the `appsettings.json` file with your SMTP server details:
   ```json
   {
     "SMTP": {
       "Host": "smtp.example.com",
       "Port": 587,
       "Username": "username@example.com",
       "Password": "yourpassword"
     }
   }
   ```

3. Build the project:
   ```bash
   dotnet build
   ```

4. Run the application:
   ```bash
   dotnet run
   ```

## Features

- Reads SMTP configuration from `appsettings.json`.
- Uses dependency injection.
- Logs operations to the console.
- Demonstrates email sending functionality using a sample email message.
