using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace MailSenderService;

class Program
{
    static void Main(string[] args)
    {
        var host = CreateHostBuilder(args).Build();

        var mailService = host.Services.GetService<IMailService>();
        mailService?.SendSampleEmail();

        host.Run();
    }

    static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureServices((hostContext, services) =>
            {
                services.Configure<SmtpConfig>(hostContext.Configuration.GetSection("SmtpConfig"));
                services.AddSingleton<IMailService, MailService>();
                services.AddLogging(config =>
                {
                    config.AddConsole();
                });
            });
}
