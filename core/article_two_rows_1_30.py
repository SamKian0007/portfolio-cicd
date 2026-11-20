"""Article 2 horizontal timeline rows 1–30 (verbatim source; dates year-month)."""

def article_two_rows_1_30():
    return [
        {
            "date": "2005",
            "title": "Puppet",
            "description": (
                "Before Puppet, administrators often configured servers manually. That led to configuration drift, "
                "where machines that were supposed to be identical slowly became different over time, making incidents "
                "harder to prevent and troubleshoot. Puppet solved this by letting teams define the desired state of "
                "systems in code and enforce that state consistently across many servers. Example: Before: one web "
                "server has a newer package version than the other, so the app behaves differently. After: Puppet "
                "applies the same package and config on both servers."
            ),
            "image": "img/solutions logs/1. puppet-technology-association.jpg",
            "image_alt": "Puppet technology illustration",
            "side": "left",
            "connector_color": "rgba(64, 224, 208, 0.88)",
        },
        {
            "date": "2006-03",
            "title": "AWS (anchored by Amazon S3 launch)",
            "description": (
                "Before AWS, infrastructure usually required buying hardware, waiting for provisioning, and operating "
                "everything in-house. That made scaling slow, expensive, and difficult to adjust to changing demand. "
                "AWS helped solve this by offering infrastructure services through APIs on a pay-as-you-go basis. S3 was "
                "especially important because it gave teams durable storage without needing to build and manage their "
                "own storage systems. Example: Before: a team buys storage hardware and waits weeks before using it. "
                "After: it creates an S3 bucket the same day and starts storing backups."
            ),
            "image": "img/solutions logs/2. Amazon Simple Storage Service Integration S3.png",
            "image_alt": "Amazon S3 and AWS integration graphic",
            "side": "right",
            "connector_color": "rgba(255, 107, 138, 0.88)",
        },
        {
            "date": "2006-10",
            "title": "TeamCity",
            "description": (
                "Before CI servers were widely adopted, integration problems were often discovered late, sometimes close "
                "to release time. TeamCity solved this by automating builds and tests whenever code changed, allowing "
                "teams to detect failures earlier and reduce the risk of broken releases caused by late integration. "
                "Example: Before: a bad commit is noticed only during release testing. After: TeamCity runs the build "
                "after the commit and reports the failure immediately."
            ),
            "image": "img/solutions logs/3. TeamCity.png",
            "image_alt": "TeamCity continuous integration branding",
            "side": "left",
            "connector_color": "rgba(125, 211, 252, 0.9)",
        },
        {
            "date": "2007-02",
            "title": "RabbitMQ",
            "description": (
                "Before message brokers were commonly used, systems often communicated directly with one another. That "
                "created tight dependencies, so if one service was slow or unavailable, other services could fail as "
                "well. RabbitMQ solved this by introducing queues between systems, allowing applications to exchange "
                "work asynchronously and making distributed systems more resilient and scalable. Example: Before: "
                "checkout waits for the email service to respond before finishing the order. After: checkout puts a "
                "message in RabbitMQ and finishes immediately."
            ),
            "image": "img/solutions logs/4. rabbitmq.png",
            "image_alt": "RabbitMQ message broker logo",
            "side": "right",
            "connector_color": "rgba(251, 191, 36, 0.9)",
        },
        {
            "date": "2008-04",
            "title": "Google App Engine",
            "description": (
                "Before platforms like App Engine, developers had to manage servers, runtime configuration, and "
                "scaling details even for relatively simple web applications. App Engine solved this by providing a "
                "platform where code could be deployed directly while much of the underlying infrastructure was handled "
                "by Google. This reduced operational overhead and accelerated application delivery. Example: Before: "
                "a team sets up VMs, web servers, and scaling rules for a small app. After: it deploys the app to App "
                "Engine and the platform handles the runtime."
            ),
            "image": "img/solutions logs/5. Google App Engine.png",
            "image_alt": "Google App Engine branding",
            "side": "left",
            "connector_color": "rgba(167, 139, 250, 0.88)",
            # Same month as next row on axis; slight left nudge so both dots are visible (Article 2 only).
            "position_pct_nudge": -1.15,
        },
        {
            "date": "2008-04",
            "title": "GitHub",
            "description": (
                "Git provided powerful version control, but collaboration around Git was still difficult for many teams. "
                "GitHub solved that by making repository hosting, code review, and collaboration workflows much easier "
                "to use at scale. It helped standardize how teams worked together on shared codebases, especially in "
                "open source and distributed development environments. Example: Before: developers send patches by "
                "email and review them manually. After: they open a pull request on GitHub and discuss the changes "
                "there."
            ),
            "image": "img/solutions logs/6. GitHub.png",
            "image_alt": "GitHub logo",
            "side": "right",
            "connector_color": "rgba(52, 211, 153, 0.88)",
        },
        {
            "date": "2008-10",
            "title": "Windows Azure",
            "description": (
                "Many enterprise teams wanted cloud capabilities but were still closely tied to Microsoft technologies "
                "and on-premises environments. Windows Azure solved this by providing a Microsoft cloud platform for "
                "hosting applications and services, making it easier for those organizations to move workloads into the "
                "cloud while staying within a familiar ecosystem. Example: Before: a .NET application runs only on "
                "local Windows servers in the company data center. After: the same kind of workload is hosted on Azure "
                "services in Microsoft's cloud."
            ),
            "image": "img/solutions logs/7. Windows Azure.jpg",
            "image_alt": "Windows Azure cloud branding",
            "side": "left",
            "connector_color": "rgba(248, 113, 113, 0.88)",
            "marker_translate_x_px": -20,
        },
        {
            "date": "2008",
            "title": "New Relic",
            "description": (
                "As applications became more distributed and always online, teams needed better visibility into "
                "performance issues in production. New Relic solved this by offering SaaS-based application performance "
                "monitoring, helping teams identify slow transactions, bottlenecks, and failures without building their "
                "own monitoring platform first. Example: Before: users say the app is slow, but the team cannot see "
                "which request is causing it. After: New Relic shows that one database query is taking too long."
            ),
            "image": "img/solutions logs/8. New Relic.png",
            "image_alt": "New Relic APM branding",
            "side": "right",
            "connector_color": "rgba(56, 189, 248, 0.9)",
            "marker_translate_x_px": 50,
        },
        {
            "date": "2009-01",
            "title": "Chef",
            "description": (
                "Manual infrastructure setup created inconsistency, repeated work, and weak change control. Chef solved "
                "this by allowing teams to describe infrastructure and system configuration in code, making environments "
                "easier to automate, reuse, review, and reproduce. It helped bring software engineering practices into "
                "infrastructure management. Example: Before: an admin installs packages and edits config files by "
                "hand on each server. After: Chef recipes apply the same setup automatically on all servers."
            ),
            "image": "img/solutions logs/9. Chef.png",
            "image_alt": "Chef automation logo",
            "side": "left",
            "connector_color": "rgba(244, 114, 182, 0.88)",
        },
        {
            "date": "2009-02",
            "title": "Redis",
            "description": (
                "Traditional databases were often too slow for workloads such as caching, session storage, counters, "
                "queues, and real-time state. Redis solved this by using an in-memory design optimized for very fast "
                "reads and writes. That made it valuable for cases where low latency was more important than the full "
                "feature set of a traditional database. Example: Before: every page load reads session data from a "
                "slower disk-based database. After: the session is read from Redis much faster."
            ),
            "image": "img/solutions logs/10. redis.png",
            "image_alt": "Redis data store logo",
            "side": "right",
            "connector_color": "rgba(250, 204, 21, 0.9)",
        },
        {
            "date": "2009-04",
            "title": "Heroku",
            "description": (
                "Deploying applications used to require significant server and platform knowledge, which slowed teams "
                "down and increased operational complexity. Heroku solved this by providing a platform where developers "
                "could push code and run applications without managing most of the underlying infrastructure. This made "
                "deployment faster and lowered the barrier to getting applications into production. Example: Before: a "
                "developer prepares servers and runtime settings before publishing the app. After: the app is deployed "
                "to Heroku with a git push."
            ),
            "image": "img/solutions logs/11. Heroku.png",
            "image_alt": "Heroku platform logo",
            "side": "left",
            "connector_color": "rgba(129, 140, 248, 0.88)",
        },
        {
            "date": "2010-02",
            "title": "Elasticsearch",
            "description": (
                "Searching logs, documents, and operational data at scale often required complex custom systems or tools "
                "that were difficult to scale. Elasticsearch solved this by providing a distributed search engine with a "
                "simple API and strong performance for large datasets. It became especially useful for log search, "
                "analytics, and operational troubleshooting. Example: Before: engineers log in to many servers and "
                "search log files one by one. After: they search all collected logs from one Elasticsearch cluster."
            ),
            "image": "img/solutions logs/13. Elasticsearch.jpg",
            "image_alt": "Elasticsearch search branding",
            "side": "right",
            "connector_color": "rgba(99, 102, 241, 0.88)",
        },
        {
            "date": "2010-03",
            "title": "Vagrant",
            "description": (
                "Development environments often differed between laptops and teams, which caused setup issues and "
                "inconsistent local behavior. Vagrant solved this by making development environments reproducible "
                "through code, allowing teams to define and recreate the same local environment more reliably across "
                "different machines. Example: Before: the application works on one developer's laptop but fails on "
                "another because the local setup is different. After: both developers start the same Vagrant "
                "environment."
            ),
            "image": "img/solutions logs/12. Vagrant.png",
            "image_alt": "Vagrant development environments branding",
            "side": "left",
            "connector_color": "rgba(14, 165, 233, 0.88)",
        },
        {
            "date": "2010",
            "title": "Sentry",
            "description": (
                "Production errors were often hidden in logs or only discovered after users reported them. Sentry solved "
                "this by centralizing application error tracking and showing where failures happened, how often they "
                "occurred, and which code paths were involved. This made production debugging faster and more structured. "
                "Example: Before: a user reports a crash and the team searches many log files to find the error. "
                "After: Sentry shows the exception, stack trace, and affected request in one place."
            ),
            "image": "img/solutions logs/14. Sentry.webp",
            "image_alt": "Sentry error tracking branding",
            "side": "right",
            "connector_color": "rgba(251, 113, 133, 0.88)",
            "marker_translate_x_px": 30,
        },
        {
            "date": "2010-09",
            "title": "Zero Trust Architecture",
            "description": (
                "Traditional security models assumed that systems inside the network perimeter were more trustworthy than "
                "systems outside it. That approach became weaker as cloud systems, remote access, and internal lateral "
                "movement by attackers became more common. Zero Trust Architecture solved this by shifting the model "
                "toward continuous verification of identity and access instead of relying on network location alone. "
                "Example: Before: a laptop connected to the internal network can reach many systems automatically. "
                "After: each access request requires identity and policy checks."
            ),
            "image": "img/solutions logs/15. Zero Trust Architecture.png",
            "image_alt": "Zero Trust Architecture concept graphic",
            "side": "left",
            "connector_color": "rgba(45, 212, 191, 0.88)",
        },
        {
            "date": "2011-02",
            "title": "AWS CloudFormation",
            "description": (
                "Early cloud adoption still involved a large amount of manual setup through web consoles. "
                "CloudFormation solved this by allowing teams to define AWS infrastructure in templates and "
                "provision it automatically. That made infrastructure more repeatable, easier to version, and "
                "easier to rebuild after failure or change. Example: Before: an engineer manually recreates servers, "
                "networks, and databases in the AWS console after a failure. After: CloudFormation recreates the "
                "environment from the template."
            ),
            "image": "img/solutions logs/16. AWS CloudFormation.png",
            "image_alt": "AWS CloudFormation placeholder graphic",
            "side": "right",
            "connector_color": "rgba(251, 191, 36, 0.9)",
        },
        {
            "date": "2011-05",
            "title": "OpenShift",
            "description": (
                "Teams wanted faster application delivery without having to assemble every platform layer themselves on "
                "raw infrastructure. OpenShift solved this by providing an application platform that reduced the amount "
                "of infrastructure work developers and operators needed to do directly, helping organizations deliver "
                "applications with more consistency and less manual setup. Example: Before: a team builds its own "
                "application platform from raw servers and middleware. After: it deploys the application on OpenShift "
                "using the platform already provided."
            ),
            "image": "img/solutions logs/17. OpenShift.png",
            "image_alt": "OpenShift placeholder graphic",
            "side": "left",
            "connector_color": "rgba(239, 68, 68, 0.88)",
        },
        {
            "date": "2011",
            "title": "Travis CI",
            "description": (
                "Many smaller teams and open-source projects needed continuous integration but did not want to run and "
                "maintain their own CI servers. Travis CI solved this by offering hosted CI that automatically built and "
                "tested code changes, making continuous integration easier to adopt and more accessible. Example: "
                "Before: contributors run tests manually before merging code. After: Travis CI runs the tests "
                "automatically for every pull request."
            ),
            "image": "img/solutions logs/18. Travis CI.png",
            "image_alt": "Travis CI placeholder graphic",
            "side": "right",
            "connector_color": "rgba(59, 130, 246, 0.88)",
            "position_pct_nudge": -1.0,
            "marker_translate_x_px": 50,
        },
        {
            "date": "2011",
            "title": "CircleCI",
            "description": (
                "Running CI infrastructure internally created maintenance overhead and slowed teams down. CircleCI solved "
                "this by providing hosted CI/CD services, reducing the operational burden of maintaining build systems and "
                "making automated testing and delivery easier to adopt. Example: Before: the team spends time fixing "
                "and maintaining its own CI server. After: CircleCI runs the pipeline as a managed service."
            ),
            "image": "img/solutions logs/19. CircleCI.png",
            "image_alt": "CircleCI placeholder graphic",
            "side": "left",
            "connector_color": "rgba(34, 211, 238, 0.88)",
            "position_pct_nudge": 1.05,
            "marker_translate_x_px": 30,
        },
        {
            "date": "2012-01",
            "title": "Apache Kafka (first Apache release)",
            "description": (
                "Older messaging systems often struggled with very large volumes of event data and real-time data movement "
                "between services. Kafka solved this by providing a distributed, durable, high-throughput event "
                "streaming platform. It became important for log pipelines, stream processing, and event-driven "
                "architectures where reliable data flow at scale was essential. Example: Before: a growing stream of "
                "application events overloads the old messaging system. After: Kafka handles the event stream and "
                "different consumers read it reliably."
            ),
            "image": "img/solutions logs/20. Apache Kafka.png",
            "image_alt": "Apache Kafka placeholder graphic",
            "side": "right",
            "connector_color": "rgba(16, 185, 129, 0.88)",
        },
        {
            "date": "2012-03",
            "title": "Ansible",
            "description": (
                "Some automation tools were effective but required agents, heavier setup, or more complex management. "
                "Ansible solved this by using an agentless model and readable YAML playbooks, making automation easier "
                "to adopt and maintain across many systems. Example: Before: the team installs and manages an agent on "
                "every server before automating anything. After: Ansible connects over SSH and applies the playbook "
                "directly."
            ),
            "image": "img/solutions logs/21. Ansible.png",
            "image_alt": "Ansible placeholder graphic",
            "side": "left",
            "connector_color": "rgba(220, 38, 127, 0.88)",
        },
        {
            "date": "2012-04",
            "title": "Firebase",
            "description": (
                "Building real-time application features traditionally required a custom backend, synchronization logic, "
                "and ongoing infrastructure work. Firebase solved this by offering a hosted real-time backend that "
                "synchronized data automatically between clients, reducing the effort needed to build interactive and "
                "live-updating applications. Example: Before: a chat app needs custom backend code to push new messages "
                "to connected users. After: Firebase syncs new messages to all clients in real time."
            ),
            "image": "img/solutions logs/22. Firebase.png",
            "image_alt": "Firebase placeholder graphic",
            "side": "right",
            "connector_color": "rgba(234, 179, 8, 0.9)",
        },
        {
            "date": "2014-06",
            "title": "Kubernetes",
            "description": (
                "Running containers individually was manageable, but operating them across many servers introduced "
                "challenges around scheduling, scaling, networking, and recovery. Kubernetes solved this by automating "
                "container orchestration, allowing teams to run containerized workloads in a more reliable, scalable, and "
                "controlled way. Example: Before: operators choose manually which server should run each container and "
                "restart failed ones themselves. After: Kubernetes schedules containers, restarts them, and scales them "
                "automatically."
            ),
            "image": "img/solutions logs/23. Kubernetes.png",
            "image_alt": "Kubernetes placeholder graphic",
            "side": "left",
            "connector_color": "rgba(99, 102, 241, 0.9)",
        },
        {
            "date": "2014-07",
            "title": "Terraform",
            "description": (
                "Cloud infrastructure was often created manually or through custom scripts that were hard to maintain and "
                "reuse. Terraform solved this by allowing infrastructure to be declared in code and applied "
                "consistently, including across multiple cloud providers. This improved reproducibility, reviewability, "
                "and change control for infrastructure work. Example: Before: an engineer creates cloud resources by "
                "clicking in the console and repeating the same steps each time. After: Terraform creates the "
                "environment from versioned code."
            ),
            "image": "img/solutions logs/24. Terraform.png",
            "image_alt": "Terraform placeholder graphic",
            "side": "right",
            "connector_color": "rgba(124, 58, 237, 0.88)",
        },
        {
            "date": "2014-11",
            "title": "AWS CodeDeploy",
            "description": (
                "Manual deployments were slow, inconsistent, and prone to human error, especially across many servers or "
                "instances. CodeDeploy solved this by automating application rollouts, helping teams standardize "
                "deployments, reduce risk, and improve release reliability. Example: Before: admins copy the new "
                "application version to each server by hand. After: CodeDeploy pushes the new version to all target "
                "servers automatically."
            ),
            "image": "img/solutions logs/25. AWS CodeDeploy.png",
            "image_alt": "AWS CodeDeploy placeholder graphic",
            "side": "left",
            "connector_color": "rgba(14, 165, 233, 0.9)",
        },
        {
            "date": "2015-07",
            "title": "AWS CodePipeline",
            "description": (
                "Build, test, and deployment stages were often spread across disconnected scripts and tools. CodePipeline "
                "solved this by providing a managed way to connect release stages into one automated workflow, making "
                "delivery pipelines more consistent and easier to operate. Example: Before: build, test, and deploy "
                "are started separately by different scripts or people. After: CodePipeline runs the stages in one "
                "connected workflow."
            ),
            "image": "img/solutions logs/26. AWS CodePipeline.png",
            "image_alt": "AWS CodePipeline placeholder graphic",
            "side": "right",
            "connector_color": "rgba(236, 72, 153, 0.88)",
        },
        {
            "date": "2015-09",
            "title": "Nomad",
            "description": (
                "As workloads spread across many machines, teams needed a reliable way to place applications and jobs "
                "automatically. Nomad solved this by providing a scheduler and workload orchestrator that reduced the "
                "need for manual placement and improved consistency in distributed environments. Example: Before: "
                "operators decide by hand which server should run each job. After: Nomad places jobs automatically on "
                "available machines."
            ),
            "image": "img/solutions logs/27. Nomad.png",
            "image_alt": "Nomad placeholder graphic",
            "side": "left",
            "connector_color": "rgba(20, 184, 166, 0.9)",
        },
        {
            "date": "2015-11",
            "title": "Helm",
            "description": (
                "Kubernetes deployments often involved many YAML files, repeated configuration, and difficult release "
                "management. Helm solved this by packaging Kubernetes applications into reusable charts, making "
                "deployment, upgrade, and sharing of complex applications easier to manage. Example: Before: a team "
                "applies many separate Kubernetes YAML files to install one application. After: Helm installs the "
                "application as one chart with reusable values."
            ),
            "image": "img/solutions logs/28. Helm.png",
            "image_alt": "Helm placeholder graphic",
            "side": "right",
            "connector_color": "rgba(96, 165, 250, 0.9)",
            "position_pct_nudge": -1.0,
            "marker_translate_x_px": 20,
        },
        {
            "date": "2015-11",
            "title": "Spinnaker",
            "description": (
                "As release frequency increased, deployments became harder to manage safely across multiple environments "
                "and cloud platforms. Spinnaker solved this by focusing on continuous delivery, deployment "
                "orchestration, rollout control, and rollback support, helping teams release software faster with more "
                "control. Example: Before: teams promote releases across environments with manual steps and risky "
                "rollback procedures. After: Spinnaker manages rollout and rollback from one delivery workflow."
            ),
            "image": "img/solutions logs/29. Spinnaker.png",
            "image_alt": "Spinnaker placeholder graphic",
            "side": "left",
            "connector_color": "rgba(245, 158, 11, 0.9)",
            "position_pct_nudge": 1.0,
        },
        {
            "date": "2016-07",
            "title": "Prometheus",
            "description": (
                "Traditional monitoring systems were often designed for static environments and did not fit modern "
                "cloud-native systems well. Prometheus solved this by providing a monitoring model suited to dynamic "
                "infrastructure, with flexible metrics collection and alerting designed for distributed services and "
                "containerized environments. Example: Before: monitoring misses short-lived containers because targets "
                "keep changing. After: Prometheus keeps discovering targets and scraping metrics as the environment "
                "changes."
            ),
            "image": "img/solutions logs/30. Prometheus.png",
            "image_alt": "Prometheus placeholder graphic",
            "side": "right",
            "connector_color": "rgba(248, 113, 113, 0.88)",
        },
    ]
