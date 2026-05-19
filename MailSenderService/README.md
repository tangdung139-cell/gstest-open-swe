# MailSenderService

This is a .NET 8 console application that demonstrates an SMTP mail sender service.

## Features

- Reads SMTP configuration from `appsettings.json`
- Implements Dependency Injection for cleaner code
- Provides robust logging capabilities
- Includes a sample function to send emails

## Getting Started

### Prerequisites

- Install .NET 8 SDK from [Microsoft's official website](https://dotnet.microsoft.com/download/dotnet/8.0).

### Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/tangdung139-cell/gstest-open-swe.git
    ```

2. Navigate to the `MailSenderService` directory:
    ```bash
    cd gstest-open-swe/MailSenderService
    ```

3. Update the `appsettings.json` file with your own SMTP configuration:
    ```json
    {
      "SmtpConfig": {
        "Host": "your-smtp-host",
        "Port": 587,
        "Username": "your-username",
        "Password": "your-password"
      }
    }
    ```

4. Build the project:
    ```bash
    dotnet build
    ```

5. Run the application:
    ```bash
    dotnet run
    ```