# Portfolio content: edit name, links, about, experience, projects, writing. Replace placeholders with your own.

from .article_two_rows_1_30 import article_two_rows_1_30
from .article_two_rows_31_56 import article_two_rows_31_56

# Second on-site article (blank template until content is added); must match path in core.urls.
ARTICLE_SECOND_SLUG = "article-2"

# Third on-site article (prose); must match path in core.urls.
ARTICLE_THIRD_SLUG = "art3"

# Fourth on-site article (prose); must match path in core.urls.
ARTICLE_FOURTH_SLUG = "art4"

# Fifth on-site article (prose); must match path in core.urls.
ARTICLE_FIFTH_SLUG = "art5"

# Sixth on-site article (prose); must match path in core.urls.
ARTICLE_SIXTH_SLUG = "art6"

# Seventh on-site article (prose); must match path in core.urls.
ARTICLE_SEVENTH_SLUG = "art7"

# Eighth on-site article (prose); must match path in core.urls.
ARTICLE_EIGHTH_SLUG = "art8"


def _build_article_two_horizontal_items():
    """Article 2 horizontal timeline - rows 1–56 (year-month dates; descriptions verbatim from source tables)."""
    return article_two_rows_1_30() + article_two_rows_31_56()


SITE = {
    "profile": {
        "name": "Samuel Parsakian",
        "role": "DevOps Engineer ",
        "tagline": "\"Make it work, make it right, make it fast.\"<br>- Kent Beck",
    },
    "social": [
        {"label": "GitHub", "url": "https://github.com/SamParsakian"},
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/samparsakian"},
    ],
    "about": [
        "I’m a DevOps Engineering student focused on Linux, Docker, Kubernetes, Git, CI/CD, scripting, databases, and cloud technologies. I have hands-on experience building and containerizing applications, automating workflows, working with deployment pipelines, and developing small systems using Python and Java.",
        "Through my projects, I’ve developed practical experience across application deployment, infrastructure workflows, automation, networking, and backend development. These projects have helped me connect what I learn with real implementation and improve my understanding of reliable systems.",
        "I also bring experience from structured, high-responsibility environments where accuracy, safety, and clear processes are essential. This has strengthened my teamwork, communication, and ability to work effectively under pressure.",
        "I’m passionate about building reliable systems, improving automation, and continuously developing my skills in cloud and DevOps technologies."
    ],
    # Update these paths when replacing CV PDFs in static/documents/
    "resume": "documents/samuel-parsakian-cv-en.pdf",
    "resume_sv": "documents/samuel-parsakian-cv-sv.pdf",
    # Standalone frontend-only builds, linked from the homepage's Vercel icon.
    # Not part of SITE["projects"] - kept lightweight (title + short desc + live link only).
    "frontend_projects": [
        {
            "slug": "med-imaging-hub",
            "title": "Med Imaging Hub",
            "desc": (
                "A bilingual (Swedish/English) frontend for a medical imaging data platform, "
                "visualizing MRI facility access and regional trends across Sweden. Shown here "
                "as the interface layer of a larger fullstack project."
            ),
            "url": "https://med-imaging-hub-web-xi74.vercel.app",
        },
        {
            "slug": "sam-medsyn-lab",
            "title": "Sam MedSyn Lab",
            "desc": (
                "An interactive Next.js frontend for a medical imaging center homepage, built "
                "with Framer Motion for responsive, motion-driven visuals."
            ),
            "url": "https://sam-medsyn-lab-frontend.vercel.app",
        },
        {
            "slug": "korkort-redo",
            "title": "Körkort Redo",
            "desc": (
                "A browser-based practice app for the Swedish driving theory test, with a "
                "280-question bank across four languages and full Farsi/Arabic RTL support. "
                "Highlighted here for its Next.js frontend and client-side practice experience."
            ),
            "url": "https://korkort-redo.vercel.app",
        },
    ],
    "experience": [
        {
            "date": "2023 - PRESENT",
            "title": "DevOps Engineer Projects",
            "org": "Personal Projects & Training",
            "bullets": [
                "Built a GitOps-based CI/CD pipeline on Azure with Azure DevOps, Terraform, AKS, and Argo CD",
                "Built and deployed a demo radiology worklist application using Docker Compose and Kubernetes on a multi-node VPS cluster",
                "Built and deployed a medical imaging DevOps platform with DICOM/PACS, anonymization, AI inference, object storage, an API, dashboard, monitoring, CI, and multi-node VPS deployment",
                "Built a Jenkins CI/CD pipeline on AWS EC2 with GitHub triggers, automated Maven testing, SonarQube quality checks, and Nexus artifact publishing",
                "Built and containerized web applications using Docker and Docker Compose",
                "Implemented CI/CD pipelines with GitHub Actions for automated testing and deployment",
                "Designed and configured a full enterprise network in Cisco Packet Tracer and CML, including OSPF routing, HSRP, IPsec VPN, VLAN segmentation, and wireless infrastructure",
                "Built and documented a Microsoft 365 tenant administration lab covering identity, Teams, SharePoint, Exchange Online, access control, security review, onboarding, offboarding, and incident response workflows",
                "Built a Node.js application integrating the OpenAI API with streaming responses and conversation memory",
                "Developed Flask-based applications integrating PostgreSQL and external APIs",
                "Designed and built a Java desktop application for structured log analysis and visualization",
                "Implemented data filtering, chart-based visualization, and reporting features across projects",
                "Automated deployment workflows to a VPS environment using secure SSH-based pipelines"
            ],
            "tags": ["Docker", "CI/CD", "GitHub Actions", "Python", "Flask", "PostgreSQL", "Java", "API"]
        },
        {
            "date": "2022 - 2025",
            "title": "Radiography Department Assistant",
            "org": "Hospitals in Sweden",
            "bullets": [
                "Worked in clinical environments with high focus on safety and accuracy",
                "Collaborated with medical teams in fast-paced settings",
                "Strengthened communication, responsibility, and structured workflows",
                "Gained experience in handling critical systems and processes"
            ],
            "tags": ["Teamwork", "Communication", "Structured Work", "Safety-Critical Environment"]
        },
    ],
    # Projects may optionally define `gallery_images` (ordered list) or `gallery_dir` (folder under `static/`) for the modal lightbox.
    "projects": [
        {
            "title": "Azure DevOps + GitOps CI/CD Pipeline",
            "slug": "azure-devops-gitops-cicd",
            "featured": True,
            "desc": (
                "A GitOps-based CI/CD platform on Azure that takes every code change from commit to the running cluster "
                "automatically: Azure Pipelines builds and versions the Docker images, and Argo CD deploys them to "
                "Kubernetes (AKS) with no manual steps."
            ),
            "highlights": [
                "Built the full Azure infrastructure as code with Terraform, including AKS, ACR, networking, and a self-hosted Azure DevOps agent",
                "Designed separate Azure Pipelines for the vote, result, and worker services, so each service builds and deploys independently",
                "Built and pushed versioned Docker images to ACR, using pipeline Build IDs as image tags for clear traceability",
                "Automated Kubernetes manifest updates with a reusable shell script, keeping Git as the single source of truth",
                "Used Argo CD for automated GitOps deployment to AKS, keeping the running cluster in sync with Git",
                "Verified the complete flow end to end with a live Snow/Rain change, from source code to the running cluster",
            ],
            "tags": ["Azure DevOps", "Azure Pipelines", "Terraform", "Docker", "ACR", "AKS", "Kubernetes", "Argo CD", "GitOps", "CI/CD", "Azure Repos", "Bash"],
            "thumb": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_01.png",
            "thumb_alt": "Architecture diagram of the Azure DevOps and GitOps CI/CD flow from code change to AKS",
            "gallery_images": [
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_01.png",
                    "alt": "Architecture diagram of the Azure DevOps and GitOps CI/CD flow from code change to AKS",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_02.png",
                    "alt": "Upstream example-voting-app repository used as the multi-service application",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_03.png",
                    "alt": "Vote app running with the original Cats vs Dogs options",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_04.png",
                    "alt": "Result app showing the live Cats vs Dogs vote percentages",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_05.png",
                    "alt": "Azure Repos diff changing the vote options from Cats and Dogs to Snow and Rain",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_06.png",
                    "alt": "kubectl output showing the vote, result, worker, Redis, and database pods running in AKS",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_07.png",
                    "alt": "kubectl deployments showing the vote, result, and worker images pulled from ACR",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_08.png",
                    "alt": "Azure Pipelines run history for the worker service CI pipeline",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_09.png",
                    "alt": "Azure resource visualizer for the AKS cluster",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_10.png",
                    "alt": "Argo CD application tree showing the vote-lab app synced and healthy",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_11.png",
                    "alt": "Argo CD resource list with all pods and services healthy and synced",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_12.png",
                    "alt": "Argo CD network view mapping each service to its pod",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_13.png",
                    "alt": "Argo CD pods view grouped by AKS node",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_14.png",
                    "alt": "Azure resource group created with Terraform, including ACR, AKS, networking, and the agent VM",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_15.png",
                    "alt": "Azure Pipelines run history for the vote service, including the Snow and Rain change",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_16.png",
                    "alt": "ACR vote-app repository listing images tagged with pipeline Build IDs",
                },
                {
                    "src": "img/projects/azure-devops-gitops-cicd/azure-devops-gitops-cicd_17.png",
                    "alt": "Argo CD automatically syncing the new vote image pushed by Azure Pipelines",
                },
            ],
        },
        {
            "title": "Medical Imaging DevOps Platform",
            "slug": "medical-imaging-devops-platform",
            "featured": True,
            "desc": (
                "A fullstack DevOps project for a demo radiology platform where medical imaging studies are "
                "received, anonymized, stored, analyzed with AI, and monitored through a complete containerized "
                "environment."
            ),
            "highlights": [
                "Built a local Docker Compose stack with Orthanc, PostgreSQL, MinIO, FastAPI, AI inference, Prometheus, and Grafana",
                "Implemented a DICOM pipeline for metadata extraction, anonymization, preview generation, and upload to S3-compatible object storage",
                "Developed a FastAPI backend API and dashboard for studies, image viewing, AI results, audit events, and operational links",
                "Integrated a separate AI inference service with TorchXRayVision DenseNet121 for chest X-ray findings, confidence scores, and heatmap generation",
                "Stored AI results, metadata, and audit logs in PostgreSQL for traceability and history",
                "Built a demo workflow for radiographer upload and doctor review with automated AI processing",
                "Added Prometheus metrics and Grafana dashboards for both the API and AI service",
                "Implemented backup and restore flows for PostgreSQL, MinIO, and Orthanc",
                "Verified CI with GitHub Actions through real push, pull request, and merge workflows",
                "Deployed the platform across three Hetzner VPS nodes for app, data/imaging, and monitoring, using a private network and one Docker Compose setup per node",
            ],
            "tags": ["Docker", "Docker Compose", "FastAPI", "Python", "PostgreSQL", "MinIO", "Orthanc", "DICOM", "AI Inference", "TorchXRayVision", "Prometheus", "Grafana", "GitHub Actions", "CI/CD", "Hetzner VPS", "Backup & Restore"],
            "thumb": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_01.png",
            "thumb_alt": "MedSyn Lab imaging platform home page showing the DICOM pipeline demo steps",
            "gallery_images": [
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_01.png",
                    "alt": "MedSyn Lab imaging platform home page showing the DICOM pipeline demo steps",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_02.png",
                    "alt": "Upload page for submitting a chest X-ray study to the pipeline",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_03.png",
                    "alt": "Ops dashboard linking to the API docs, MinIO console, Orthanc explorer, Prometheus, and Grafana",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_04.png",
                    "alt": "Hetzner Cloud console showing the three VPS nodes for the app, data, and ops tiers",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_05.png",
                    "alt": "NIH Chest X-ray dataset sample used for AI inference testing",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_06.png",
                    "alt": "Orthanc DICOM server web interface showing a stored study",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_07.png",
                    "alt": "MinIO object storage browser showing an anonymized DICOM preview",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_08.png",
                    "alt": "FastAPI Swagger documentation for the Medical Imaging Study API",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_09.png",
                    "alt": "Docker Desktop showing the running imaging pipeline containers",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_10.png",
                    "alt": "Medical imaging dashboard showing a study with AI inference results and a heatmap",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_11.png",
                    "alt": "Doctor review page showing an uploaded study with AI findings and heatmap",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_12.png",
                    "alt": "DICOM pipeline demo walking through each processing step",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_13.png",
                    "alt": "Grafana dashboard showing API health and request metrics",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_14.png",
                    "alt": "Prometheus target health showing the API and AI inference services as up",
                },
                {
                    "src": "img/projects/medical-imaging-devops-platform/medical-imaging-devops-platform_15.png",
                    "alt": "Architecture diagram of the imaging pipeline and three-node Hetzner deployment",
                },
            ],
        },
        {
            "title": "Radiology ScanFlow",
            "slug": "radiology-scanflow",
            "featured": True,
            "desc": (
                "A full-stack DevOps project for a demo radiology worklist application, built with React, "
                "Node.js, Express, and MongoDB. The application was first containerized with Docker Compose and "
                "then deployed to a real Kubernetes cluster across three VPS instances, including persistent "
                "storage, NodePort access, pod self-healing, node drain testing, and cluster visualization with Lens."
            ),
            "highlights": [
                "Built a React frontend for viewing, adding, and deleting demo imaging cases",
                "Built a Node.js and Express backend API connected to MongoDB",
                "Containerized the frontend, backend, and database with Docker Compose",
                "Wrote Kubernetes manifests for the frontend, backend, MongoDB, services, and persistent storage",
                "Deployed the application to a three-node Kubernetes cluster on VPS infrastructure",
                "Demonstrated Kubernetes self-healing by deleting pods and observing automatic replacement",
                "Simulated node failure with node drain and verified pod rescheduling",
                "Used Lens to visually inspect pods, services, logs, and deployments across the cluster",
            ],
            "tags": ["Docker", "Docker Compose", "Kubernetes", "React", "Node.js", "MongoDB", "Self-Healing", "Lens"],
            "thumb": "img/projects/radiology-scanflow/radiology-scanflow_01.png",
            "thumb_alt": "Radiology ScanFlow worklist showing imaging cases",
            "gallery_images": [
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_01.png",
                    "alt": "Radiology ScanFlow worklist showing imaging cases",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_02.png",
                    "alt": "Docker Desktop showing the running ScanFlow containers",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_03.png",
                    "alt": "Docker Desktop showing the built ScanFlow frontend and backend images",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_04.png",
                    "alt": "Terminal listing the ScanFlow and MongoDB Docker images",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_05.png",
                    "alt": "Terminal output building the Docker Compose stack",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_06.png",
                    "alt": "Terminal output starting the frontend, backend, and database containers",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_07.png",
                    "alt": "ScanFlow backend API health check responding in the browser",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_08.png",
                    "alt": "Three-node Kubernetes cluster running on Hetzner VPS infrastructure",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_09.png",
                    "alt": "Firewall applied to the Kubernetes cluster servers",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_10.png",
                    "alt": "Firewall rules restricting SSH, API server, and NodePort access",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_11.png",
                    "alt": "Private network configured for the Kubernetes cluster nodes",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_12.png",
                    "alt": "Kubernetes control plane version after cluster initialization",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_13.png",
                    "alt": "Cluster pods running across the control plane and worker nodes",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_14.png",
                    "alt": "ScanFlow frontend, backend, and database pods running in the cluster",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_15.png",
                    "alt": "Radiology ScanFlow worklist running live on the Kubernetes cluster",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_16.png",
                    "alt": "Kubernetes self-healing replacing a deleted pod automatically",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_17.png",
                    "alt": "Draining a worker node and rescheduling its pods",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_18.png",
                    "alt": "ScanFlow pods inspected visually in Lens",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_19.png",
                    "alt": "Cluster nodes inspected in Lens with cordon and drain options",
                },
                {
                    "src": "img/projects/radiology-scanflow/radiology-scanflow_20.png",
                    "alt": "Second worker node drained and its pods rescheduled",
                },
            ],
        },
        {
            "title": "Jenkins CI/CD Pipeline on AWS",
            "slug": "jenkins-cicd-aws",
            "featured": True,
            "desc": (
                "A Jenkins-driven CI pipeline for a Maven Java application, with GitHub triggers, "
                "automated tests, SonarQube quality gates, and Nexus artifact publishing on separate AWS EC2 hosts."
            ),
            "highlights": [
                "Built a Jenkins pipeline triggered from GitHub changes",
                "Compiled and tested a Maven Java application automatically",
                "Integrated SonarQube for code quality checks and quality gate validation",
                "Published build artifacts to Nexus Repository",
                "Used separate AWS EC2 instances for Jenkins, SonarQube, and Nexus",
                "Demonstrated a full CI workflow from code push to artifact storage",
            ],
            "tags": [
                "Jenkins",
                "AWS EC2",
                "GitHub",
                "Maven",
                "Java",
                "SonarQube",
                "Nexus",
                "CI/CD",
            ],
            "thumb": "img/projects/jenkins-cicd-aws/jenkins_01.png",
            "thumb_alt": "AWS EC2 instances for Jenkins, SonarQube, and Nexus",
            "gallery_images": [
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_01.png",
                    "alt": "AWS EC2 instances for Jenkins, SonarQube, and Nexus",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_02.png",
                    "alt": "AWS EC2 launch configuration for Nexus CI server",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_03.png",
                    "alt": "Jenkins installation on Linux",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_04.png",
                    "alt": "Jenkins setup wizard installing CI/CD plugins",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_05.png",
                    "alt": "Maven clean test build success",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_06.png",
                    "alt": "Maven clean package producing JAR artifact",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_07.png",
                    "alt": "SonarQube Scanner configured in Jenkins",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_08.png",
                    "alt": "SonarQube quality gate passed for sample app",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_09.png",
                    "alt": "Nexus Repository hosted Maven releases",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_10.png",
                    "alt": "Jenkins pipeline with SonarQube quality gate and artifacts",
                },
                {
                    "src": "img/projects/jenkins-cicd-aws/jenkins_11.png",
                    "alt": "Maven snapshot artifacts published in Nexus",
                },
            ],
        },
        {
            "title": "Notes CI/CD App",
            "slug": "notes-cicd-app",
            "featured": False,
            "desc": "A simple Flask notes application featuring containerization, automated testing, and deployment to a Hetzner VPS.",
            "highlights": [
                "Create and delete notes through a simple web interface",
                "Store notes in a PostgreSQL database",
                "Run the app and database together with Docker Compose",
                "Test the project automatically with GitHub Actions CI",
                "Deploy automatically to a Hetzner VPS with GitHub Actions over SSH",
                "Demonstrates a full workflow from code push to test and deployment"
            ],
            "tags": ["Flask", "PostgreSQL", "Docker", "GitHub Actions", "CI/CD", "Hetzner"],
            "thumb": "img/projects/CICD-1-NoteApplication/CICD_1_01.png",
            "thumb_alt": "Notes CI/CD App main preview",
            "gallery_images": [
                {
                    "src": "img/projects/CICD-1-NoteApplication/CICD_1_01.png",
                    "alt": "Notes CI/CD App main preview"
                },
                {
                    "src": "img/projects/CICD-1-NoteApplication/CICD_1_02.png",
                    "alt": "Notes CI/CD App screenshot"
                },
                {
                    "src": "img/projects/CICD-1-NoteApplication/CICD_1_03.png",
                    "alt": "Notes CI/CD App screenshot"
                },
                {
                    "src": "img/projects/CICD-1-NoteApplication/CICD_1_04.png",
                    "alt": "Notes CI/CD App screenshot"
                }
            ],
        },
        {
            "title": "AI Conversation Engine (OpenAI API in Node.js)",
            "slug": "ai-conversation-engine",
            "featured": False,
            "desc": (
                "A Node.js application demonstrating practical integration with the OpenAI Responses API - "
                "covering authenticated requests, parameter tuning, conversation memory, and real-time streaming."
            ),
            "highlights": [
                "Built an authenticated client for the OpenAI Responses API",
                "Sent requests and parsed responses, including token usage and metadata",
                "Tuned output behavior using temperature and max_output_tokens",
                "Maintained conversation context across multiple calls using response IDs",
                "Implemented real-time streaming of model output, token by token",
                "Secured API credentials using environment variables, excluded from version control",
            ],
            "tags": ["Node.js", "OpenAI API", "JavaScript", "REST API", "dotenv", "Streaming", "LLM"],
            "thumb": "img/projects/ai-conversation-engine/ai-conversation-engine_04.png",
            "thumb_alt": "Node.js client code calling the OpenAI Responses API with streaming enabled",
            "gallery_images": [
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_01.png",
                    "alt": "Creating a new OpenAI API key for the project",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_02.png",
                    "alt": "Active OpenAI API key used by the application",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_04.png",
                    "alt": "Node.js client code calling the OpenAI Responses API with streaming enabled",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_05.png",
                    "alt": "Conversation memory logic using response IDs",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_03.png",
                    "alt": "Git history showing incremental development of the API integration",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_06.png",
                    "alt": "Exploring OpenAI's tokenizer to understand token usage",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_07.png",
                    "alt": "Sample API response logged in the OpenAI dashboard",
                },
                {
                    "src": "img/projects/ai-conversation-engine/ai-conversation-engine_08.png",
                    "alt": "Additional response log showing model output",
                },
            ],
        },
        {
            "title": "MedSyn Lab - Enterprise Network Design",
            "slug": "medsyn-lab-network",
            "featured": True,
            "desc": (
                "A complete enterprise network designed and implemented in Cisco Packet Tracer and Cisco Modeling Labs, "
                "covering routing, switching, security, VPN, and high availability for a fictional medical company "
                "with HQ and branch sites."
            ),
            "highlights": [
                "Designed a dual-ISP, dual-firewall HQ architecture with full redundancy",
                "Configured OSPF routing and HSRP gateway redundancy across all VLANs at both sites",
                "Implemented IPsec site-to-site VPN between HQ and branch office",
                "Set up VLAN segmentation with 802.1Q trunking across 9 departments",
                "Deployed WLC-managed wireless network with CAPWAP lightweight APs",
                "Verified full connectivity - all tests passed across HQ, branch, DMZ, and VPN",
            ],
            "tags": ["Cisco", "Packet Tracer", "CML", "OSPF", "VLAN", "IPsec", "HSRP", "Networking"],
            "thumb": "img/projects/medsyn-lab-network/network_topology.jpg",
            "thumb_alt": "Full MedSyn Lab network topology diagram",
            "gallery_images": [
                {
                    "src": "img/projects/medsyn-lab-network/network_topology.jpg",
                    "alt": "Full network topology diagram (Packet Tracer)",
                },
                {
                    "src": "img/projects/medsyn-lab-network/01_topology-overview.png",
                    "alt": "Full lab topology overview in Cisco Modeling Labs",
                },
                {
                    "src": "img/projects/medsyn-lab-network/02_HQ-department-groups.png",
                    "alt": "HQ department groups - MgmtAdmin, BizOps, Finance, TechOps, ITInfra",
                },
                {
                    "src": "img/projects/medsyn-lab-network/03_WAN-core-DMZ-area.png",
                    "alt": "WAN core, ISPs, firewalls, and DMZ cluster",
                },
                {
                    "src": "img/projects/medsyn-lab-network/06_Branch-topology-workbench.png",
                    "alt": "Branch site topology with CoreSW1/2 and access switches",
                },
                {
                    "src": "img/projects/medsyn-lab-network/07_HQ-MgmtAdmin-BizOps-groups.png",
                    "alt": "HQ MgmtAdmin and BizOps groups close-up",
                },
                {
                    "src": "img/projects/medsyn-lab-network/08_MgmtAdmin-SW1-running-config.png",
                    "alt": "SMLC-HQ-MgmtAdmin-SW1 running configuration",
                },
                {
                    "src": "img/projects/medsyn-lab-network/09_HQ-FW1-running-config.png",
                    "alt": "SMLC-HQ-FW1 (Cisco ASA) running configuration",
                },
                {
                    "src": "img/projects/medsyn-lab-network/10_ISP-HQ1-running-config.png",
                    "alt": "ISP-HQ1 router running configuration",
                },
            ],
        },
        {
            "title": "LogInsight",
            "slug": "loginsight",
            "featured": False,
            "desc": "A Java desktop application for viewing, filtering, and analyzing log files. It helps users understand system activity through structured filtering, visualization, and reporting.",
            "highlights": [
                "Load and analyze structured log files",
                "Filter logs by date, time, level, source, user, and IP",
                "Visualize logs with charts for activity over time, level distribution, and top sources",
                "Add notes to log entries for tracking and review",
                "Export reports in Text, JSON, and CSV formats",
                "Includes a simple authentication system with predefined users"
            ],
            "tags": ["Java", "JavaFX", "Maven", "SQLite"],
            "thumb": "img/projects/loginsight_img/loginsight_03.png",
            "thumb_alt": "LogInsight graph view dashboard",
            "gallery_images": [
                {
                    "src": "img/projects/loginsight_img/loginsight_01.png",
                    "alt": "LogInsight login screen"
                },
                {
                    "src": "img/projects/loginsight_img/loginsight_02.png",
                    "alt": "LogInsight graph dashboard with filters and charts"
                },
                {
                    "src": "img/projects/loginsight_img/loginsight_03.png",
                    "alt": "LogInsight table view with filtered log records"
                },
                {
                    "src": "img/projects/loginsight_img/loginsight_05.png",
                    "alt": "LogInsight user management screen"
                },
                {
                    "src": "img/projects/loginsight_img/loginsight_04.png",
                    "alt": "LogInsight login dialog"
                }
            ]
        },
        {
            "title": "Job Explorer",
            "slug": "job-explorer",
            "featured": False,
            "desc": "A Flask application for exploring and analyzing Swedish job listings using the JobTech API, with filtering, visualization, and optional email summaries.",
            "highlights": [
                "Fetch and display job listings from the JobTech public API",
                "Filter jobs by keywords, location, and attributes",
                "View results in a structured table format",
                "Visualize job distribution by city using charts",
                "Optional email summary feature using SendGrid or SMTP",
                "Includes test suite with mocked API interactions"
            ],
            "tags": ["Flask", "API", "Python", "Data Visualization", "SendGrid", "SMTP"],
            "thumb": "img/projects/job-notifier/job_explorer_notifier_01.png",
            "thumb_alt": "Job Explorer main preview",
            "gallery_images": [
                {
                    "src": "img/projects/job-notifier/job_explorer_notifier_01.png",
                    "alt": "Job Explorer main preview"
                },
                {
                    "src": "img/projects/job-notifier/job_explorer_notifier_02.png",
                    "alt": "Job Explorer screenshot"
                },
                {
                    "src": "img/projects/job-notifier/job_explorer_notifier_03.png",
                    "alt": "Job Explorer screenshot"
                }
            ],
        },
        {
            "title": "Online Laptop Store",
            "slug": "online-laptop-store",
            "featured": False,
            "desc": "A full-stack Flask web application for browsing and purchasing laptops, featuring a complete shopping flow and an admin management system.",
            "highlights": [
                "Browse products and view detailed laptop pages",
                "Add to cart and complete a simple checkout process",
                "Admin dashboard for managing products, orders, and payments",
                "Clean, responsive UI with structured backend architecture"
            ],
            "tags": ["Flask", "Python", "SQLite", "Bootstrap"],
            "thumb": "img/projects/laptop-store-flask/laptop_01.png",
            "thumb_alt": "Online Laptop Store home page",
            "gallery_dir": "img/projects/laptop-store-flask",
        },
        {
            "title": "Portfolio Website",
            "slug": "portfolio",
            "featured": True,
            "desc": "A minimal Django portfolio template designed to showcase profile, experience, projects, and articles with both overview sections and dedicated pages.",
            "highlights": [
                "Structured layout with main sections and separate pages for deeper content",
                "Designed for easy content editing and reuse via configuration",
                "Clean and minimal interface focused on readability",
                "Supports linking to external resources like PDF résumé and project details"
            ],
            "tags": ["Django", "Python", "HTML", "CSS"],
            "thumb": "img/projects/Portfolio_website_img/portfolio_01.png",
            "thumb_alt": "Portfolio template overview section",
            "gallery_dir": "img/projects/Portfolio_website_img",
        },
        {
            "title": "MedSyn Microsoft 365 Tenant Administration",
            "slug": "medsyn-m365-admin",
            "featured": False,
            "desc": (
                "A Microsoft 365 administration lab for a fictional medical technology company, built end-to-end "
                "from business requirements into a structured tenant - covering identity, licensing, Teams, "
                "SharePoint, Exchange Online, security review, and documented admin workflows."
            ),
            "highlights": [
                "Prepared a PowerShell environment with Microsoft Graph, Exchange Online, Teams, and PnP modules; captured the tenant baseline before any configuration changes",
                "Created staff, admin-only, and break-glass accounts from CSV data; assigned Microsoft 365 Business Basic licenses and documented limitations",
                "Configured Microsoft 365 groups, security groups, distribution lists, and shared mailboxes",
                "Built Teams workspaces and channels for departments and branches; configured SharePoint sites with group-based permissions and external sharing disabled",
                "Added Exchange Online mail flow rules for external sender warnings and risky attachment blocking; reviewed Security Defaults, Service Health, and guest access settings",
                "Tested onboarding, offboarding, mailbox cleanup, session revocation, and incident response workflows; exported the final tenant configuration as documented evidence",
            ],
            "tags": [
                "Microsoft 365",
                "Entra ID",
                "PowerShell",
                "Microsoft Graph",
                "Exchange Online",
                "Teams",
                "SharePoint",
                "PnP PowerShell",
                "Identity Management",
                "Access Control",
                "Mail Flow",
                "Incident Response",
            ],
            "thumb": "img/projects/medsyn-m365-admin/medsyn-m365-admin_01.png",
            "thumb_alt": "Microsoft 365 admin portal tenant overview",
            "gallery_images": [
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_01.png",
                    "alt": "Microsoft 365 admin portal tenant overview"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_02.png",
                    "alt": "PowerShell environment with Microsoft 365 modules installed"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_03.png",
                    "alt": "Tenant baseline captured before configuration changes"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_04.png",
                    "alt": "User accounts created from CSV source data"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_05.png",
                    "alt": "Microsoft 365 Business Basic licenses assigned to users"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_06.png",
                    "alt": "Microsoft 365 groups and security groups configured"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_07.png",
                    "alt": "Distribution lists and shared mailboxes created"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_08.png",
                    "alt": "Teams workspaces and department channels set up"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_09.png",
                    "alt": "SharePoint sites with folder structures and group-based permissions"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_10.png",
                    "alt": "External sharing disabled across SharePoint sites"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_11.png",
                    "alt": "Exchange Online mail flow rule for external sender warnings"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_12.png",
                    "alt": "Exchange Online rule blocking risky attachment types"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_13.png",
                    "alt": "Service Health and Message Center review"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_14.png",
                    "alt": "Security Defaults and guest access settings reviewed"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_15.png",
                    "alt": "Group membership scope and access control verified"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_16.png",
                    "alt": "Onboarding workflow tested for new staff accounts"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_17.png",
                    "alt": "Offboarding workflow with mailbox cleanup and session revocation"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_18.png",
                    "alt": "Incident response actions tested in the tenant"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_19.png",
                    "alt": "Identity and permissions configuration exported as evidence"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_20.png",
                    "alt": "Exchange Online and Teams configuration exported"},
                {"src": "img/projects/medsyn-m365-admin/medsyn-m365-admin_21.png",
                    "alt": "Final tenant configuration summary across all workloads"},
            ],
        },
        {
            "title": "Windows Server Enterprise Lab",
            "slug": "windows-server-enterprise-lab",
            "featured": False,
            "desc": "A production-style Windows Server environment simulating a secure enterprise infrastructure, focused on Active Directory design, access control, and system management best practices.",
            "highlights": [
                "Deploy and configure Active Directory domain (corp.local)",
                "Design structured OU hierarchy for Lund and Stockholm locations",
                "Implement Group Policy for user and computer management",
                "Configure DNS with forwarders and conditional forwarding",
                "Set up centralized file server with NTFS and share permissions",
                "Apply RBAC using AGDLP model (no direct user permissions)",
                "Delegate administration using security groups",
                "Automate bulk user creation with PowerShell",
                "Deploy printers via Group Policy",
                "Enforce security policies including restricted environments and admin controls",
            ],
            "tags": [
                "Windows Server",
                "Active Directory",
                "Group Policy",
                "DNS",
                "PowerShell",
                "RBAC",
                "AGDLP",
                "File Server",
                "Enterprise Lab",
            ],
            "thumb": "img/projects/Windows_Server_Project/Windows_Server_Porj01.png",
            "thumb_alt": "Windows Server Enterprise Lab preview",
            "gallery_dir": "img/projects/Windows_Server_Project",
        },
    ],
    # External writing cards (thumbnails) on home and /articles/; empty until you add real posts.
    "writing": [],
    # Plain article pages (non-timeline), keyed by URL slug (see ARTICLE_SECOND_SLUG).
    "article_pages": {
        ARTICLE_SECOND_SLUG: {
            "heading": "Key Milestones in DevOps, Cloud, and Platform Engineering",
            "description": (
                "A journey through the tools and ideas that transformed software from manual server work into "
                "fast, automated, and scalable systems."
            ),
            "items": _build_article_two_horizontal_items(),
        },
    },
    # Document-style articles (prose + optional media), keyed by URL slug (see ARTICLE_*_SLUG).
    "article_documents": {
        ARTICLE_THIRD_SLUG: {
            "page_title": "Large-Scale Cluster Management at Google with Borg",
            "body_paragraphs": [
                "<em>Large-Scale Cluster Management at Google with Borg</em> by Abhishek Verma, Luis Pedrosa, Madhukar Korupolu, David Oppenheimer, Eric Tune, and John Wilkes is one of the foundational articles on large-scale infrastructure operations. It explains how Google designed and ran a cluster management system capable of supporting massive workloads with high efficiency, reliability, and control.",
                "This article matters because it shows how Google handled infrastructure at a scale where ordinary scheduling and operations practices were no longer enough. Borg was built to admit jobs, place them on machines, restart them after failure, monitor them continuously, and keep services available across clusters that could contain tens of thousands of machines. What makes the paper stand out is that it does not simply describe a system. It explains the thinking behind it, where reliability, efficiency, and scale are treated as one connected problem.",
                "One of the most important ideas in the article is that large infrastructure should not waste capacity simply because workloads behave differently. Borg runs long-lived production services alongside lower-priority batch work, and the paper shows why that matters. Instead of separating these workloads into completely isolated environments, Borg uses scheduling, priorities, and isolation mechanisms so that spare capacity can be used rather than left idle. In the paper\u2019s evaluation, separating production and non-production work into different cells would have required about 20\u201330% more machines in the median case.",
                "Another especially interesting point is resource reclamation. This is one of the clearest examples in the paper of how careful platform design can create major gains. Many workloads request more CPU or memory than they actually use most of the time, either for safety or to cover rare spikes. Borg measures actual usage, estimates what a task really needs, and reclaims the unused portion for lower-priority work. The important detail is that production tasks remain protected, while batch tasks make use of capacity that would otherwise sit unused. The paper shows that without this mechanism, many more machines would be needed, and that about 20% of the workload in a median cell ran in reclaimed resources.",
                "One of the strongest parts of the paper is its very practical view of failure. Machines fail, tasks crash, agents lose contact, and networks split. Borg was designed around that reality. It automatically reschedules work, spreads tasks across failure domains to reduce correlated failures, and keeps already-running tasks alive even if the master or local agent goes down. The paper reports that Borgmaster achieved about 99.99% availability in practice. That detail alone says a lot about the gap between a system that looks good on paper and one that survives real production pressure over many years.",
                "Another valuable lesson in the article is that orchestration is much more than starting processes. Borg included a declarative job specification model, stable naming, health checking, monitoring, and tools that helped users understand why jobs were pending or how they were behaving at runtime. In other words, the platform was designed not only to run workloads, but also to make them observable and manageable. That is one reason the paper still feels modern. It describes a complete operational system, not just a scheduler.",
                "The paper also challenges a few assumptions that seem reasonable at first glance. Fixed resource buckets, for example, sound simple, but Borg\u2019s workload did not fit neatly into them. The evaluation showed that rounding CPU and memory requests into bucketed sizes would have required around 30\u201350% more resources in the median case. That is a strong reminder that convenience in platform design can become waste at scale. Fine-grained resource control was not a small detail in Borg; it was one of the reasons the system could operate so efficiently.",
                "What stands out most in this article is how grounded it is in real operations. Borg is not presented as a perfect system. It is presented as a set of trade-offs tested in production over many years: sharing versus isolation, efficiency versus safety margins, centralized control versus resilience, and simplicity for users versus complexity inside the platform itself. That is exactly why the paper remains worth reading. It gives a clear picture of what serious infrastructure engineering looks like when scale, cost, and reliability all matter at the same time.",
            ],
        },
        ARTICLE_FOURTH_SLUG: {
            "page_title": "Borg, Omega, and Kubernetes",
            "body_paragraphs": [
                "<em>Borg, Omega, and Kubernetes</em> by Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer, and John Wilkes is an important article about how Google improved the way it runs applications at very large scale. It shows how container management evolved over time and why those changes mattered for reliability, efficiency, and the everyday work of operating large systems.",
                "What makes this article especially valuable is that it does not describe Kubernetes as an isolated idea or a sudden breakthrough. Instead, it shows the long path that led to it. Borg brought long-running services and batch jobs into one system, which helped Google use machines more efficiently. Omega kept many of the same foundations but moved toward a more flexible design built around shared cluster state. Kubernetes carried those lessons forward with cleaner APIs, a more consistent structure, and a stronger focus on making applications easier to deploy and manage.",
                "One of the clearest ideas in the article is that containers changed more than technical isolation. They changed the way infrastructure was understood. Instead of treating the machine as the main thing to manage, these systems increasingly treated the application as the center of operations. That shift made a real difference. Deployment, monitoring, logging, and recovery all became easier to handle because the platform could work around the needs and identity of the application itself.",
                "The article also explains why workload sharing mattered so much. Google used containers to run long-running services and batch jobs on the same machines, which improved resource usage without losing control over important services. That balance between efficiency and protection is one of the most useful parts of the article. At the same time, the authors are careful not to make the system sound perfect. They point out that isolation still has limits and that some problems remain difficult even in mature platforms.",
                "Another strong part of the article is the way it connects design choices to operational results. Kubernetes is presented as a system that learned from earlier complexity. It separates the desired state from the current state and uses controllers to keep moving the real system back toward the intended one. That idea helps explain why the platform is more stable and easier to recover when failures happen. The article also shows why smaller components with clear roles often age better than one large central system that becomes harder to change over time.",
                "Some of the most interesting examples are very practical. In Borg, networking became more complicated because containers shared the host IP address and had assigned port numbers. Kubernetes improved this by giving each pod its own IP address, which made networking much easier to understand and manage. The same kind of improvement appears in workload grouping. Borg relied on numbered task groups, while Kubernetes used labels and label selectors, which gave much more flexibility in how workloads could be organized and managed.",
                "Just as importantly, the article is honest about what is still hard. Configuration can still become too complex, especially when too much logic is pushed into it. Dependency management is also presented as a difficult problem, because service relationships are not always easy to describe or automate cleanly. These sections make the article stronger because they show that even well-designed systems still have unresolved challenges.",
                "Overall, this article is worth reading because it explains how modern container platforms improved through real experience, not through one perfect design from the start. It brings together efficiency, scheduling, isolation, API design, failure handling, and observability in a clear and grounded way. More than that, it shows how infrastructure becomes better over time: by learning from real problems, reducing unnecessary complexity, and making systems easier to operate.",
            ],
        },
        ARTICLE_FIFTH_SLUG: {
            "page_title": "Chaos Engineering for Databases",
            "body_paragraphs": [
                "In Chaos Engineering for Databases, Thanh Long Tran looks at a simple but serious question: what happens when hardware memory errors reach a running database? The article focuses on bit flips in memory and shows that the danger is not only system crashes. In some cases, a database can keep running and still return wrong results, which makes the problem much harder to notice.",
                "The work applies chaos engineering ideas to databases by creating fault-injection experiments. Instead of only studying failure in theory, the author tests how real database systems behave when faults are introduced during query execution. This makes the study practical and important, because modern systems depend heavily on correct data, not just on uptime.",
                "One of the most interesting parts of the article is how clearly it shows the difference between visible failure and silent failure. A crash is obvious. Wrong data is not. The experiments show that databases such as SQLite and DuckDB can sometimes produce incorrect results after memory faults, even when they do not stop running. That makes this kind of issue especially risky in real systems, where bad data can spread before anyone notices it.",
                "The article also shows that different database designs react differently to the same kind of fault. SQLite uses less memory, but it can still suffer from corrupted results, especially during write operations. DuckDB, which is built for analytical workloads and uses much more memory, becomes a larger target for faults during execution. This is a useful reminder that performance-focused systems may also need stronger protection when they handle important data.",
                "Another valuable part of the article is that it does not stop at showing the problem. It also looks at possible solutions. The study tests protection methods in DuckDB to detect bit flips during query execution. Some of these methods reduce silent corruption very well, which is encouraging. At the same time, the stronger protections also slow the system down a lot. That trade-off is one of the key lessons in the article: better safety is possible, but it may come with a real performance cost.",
                "What makes this article worth reading is that it explains reliability in a deeper way. A system is not truly reliable just because it stays online. It also needs to keep data correct under stress. The article makes that point in a clear and convincing way, and it shows that software-level protection can help, even if the current solutions still need improvement.",
            ],
        },
        ARTICLE_SIXTH_SLUG: {
            "page_title": "The Calculus of Service Availability",
            "body_paragraphs": [
                "<em>The Calculus of Service Availability</em> by Ben Treynor, Mike Dahlin, Vivek Rau, and Betsy Beyer explores a simple but important truth in large systems: a service is only as available as the dependencies it relies on.",
                "The article shows why reliability cannot be treated as a vague goal. It has to be understood in practical terms and built into the design of the system. When a service depends on databases, storage, caches, RPC services, or other internal platforms, each of those dependencies shapes what users actually experience. Strong availability does not come from making one service look reliable on its own. It comes from understanding the full chain behind it and designing around its limits.",
                "One of the most useful ideas in the article is the \u201cextra 9\u201d rule. If a service aims for 99.99% availability, its critical dependencies usually need to be even more reliable. Otherwise, too much of the service\u2019s allowed downtime is lost to dependency failures before its own problems are even counted. This makes reliability feel much more concrete: it is not just a target for one team, but a shared responsibility across the whole system.",
                "The article is especially valuable because it connects availability to day-to-day operations. Reliability is shaped by how often outages happen, how wide their impact is, and how quickly recovery begins. In practice, that means careful rollouts, isolation between shards or regions, fast detection, quick rollback, graceful degradation, and designs that reduce the blast radius of failure. A strong system is not one that never has problems, but one that limits damage and recovers quickly.",
                "Another important lesson is that not every dependency should remain critical. Whenever possible, a system should keep working in a reduced but acceptable way instead of failing completely. The article highlights approaches such as fallback behavior, asynchronous design, redundancy, and automated failover. These choices make systems more resilient because they reduce the chance that one broken part will bring down everything else.",
                "The article also makes clear that better reliability comes with trade-offs. More resilience often means more planning, more testing, more careful engineering, and sometimes higher cost. Redundancy, geographic isolation, and extra capacity can improve availability, but they also add complexity. The strength of the article is that it presents this honestly and shows that reliability becomes far more achievable when it is designed in from the beginning instead of added later as a fix.",
            ],
        },
        ARTICLE_SEVENTH_SLUG: {
            "page_title": "The 2015 State of DevOps Report",
            "body_paragraphs": [
                "<em>The 2015 State of DevOps Report</em> by Puppet Labs explores what separates high-performing IT organizations from the rest, and why those differences matter across the business.",
                "At the heart of the report is a clear idea: delivering software quickly does not have to come at the cost of reliability. The strongest teams in the study were able to release changes far more often while also seeing fewer failures and recovering much faster when incidents occurred. That matters because it challenges the old belief that speed creates instability. In this report, strong delivery performance is shown as the result of disciplined engineering rather than risky acceleration.",
                "The report points to a group of practices that consistently support better outcomes. Continuous integration, automated testing, deployment automation, and version control all help teams detect issues earlier and move changes through delivery with more confidence. Lean practices matter just as much. Limiting work in progress, making bottlenecks visible, and using monitoring data to support decisions all help reduce waste and improve flow. Together, these practices create an environment where teams can move faster without losing control.",
                "Another important contribution of the report is its view on architecture. It argues that performance is shaped less by whether a system is new or old, and more by whether it is designed for testability, fast feedback, and independent deployment. Systems become easier to change when they are less tightly coupled and when services can be tested and released without depending on large, fragile integrations. In that sense, architecture is presented as a practical delivery concern, not just a design topic.",
                "The report also makes a strong link between technical results and the way organizations are run. Better outcomes are associated with healthier cultures, clearer goals, visible metrics, learning from failure, and leaders who support improvement rather than simply pushing more work through the system. Painful deployments, blame-heavy environments, and constant firefighting are shown not as isolated technical problems, but as signs of deeper weaknesses in the way work is managed.",
                "One of the report\u2019s most lasting strengths is that it connects delivery performance, software design, leadership, and team health into one picture. It shows that better software delivery does not come from one tool, one framework, or one isolated change. It comes from a set of reinforcing choices that make systems easier to build, easier to release, and easier to operate over time.",
            ],
        },
        ARTICLE_EIGHTH_SLUG: {
            "page_title": "Continuous Deployment at Facebook and OANDA",
            "body_paragraphs": [
                "<em>Continuous Deployment at Facebook and OANDA</em> by Tony Savor, Mitchell Douglas, Michael Gentili, Laurie Williams, Kent Beck, and Michael Stumm explores how two very different companies used continuous deployment in real production environments.",
                "The article shows that releasing software often does not have to mean more chaos or lower quality. Instead of saving changes for large and stressful release days, both companies worked with small updates, fast feedback, and strong automation. That made it easier to move quickly, catch problems earlier, and keep development closely connected to what was happening in production.",
                "One of the most interesting ideas in the article is that speed came from discipline, not from cutting corners. Developers were expected to take ownership of their work from start to finish. They wrote the code, tested it, reviewed it, helped release it, and stayed close to it after deployment. Release engineering also played an important role by helping manage risk, coordinate deployments, and keep the process reliable.",
                "The article is also valuable because it looks at what happens as systems grow. At Facebook, the company kept shipping at a high pace even as the engineering team and codebase became much larger. That is a strong reminder that growth does not always have to slow everything down, as long as the process is designed well and supported by good tools.",
                "At the same time, the paper is honest about the trade-offs. Continuous deployment needs strong internal systems, supportive leadership, and engineers who can think about quality, performance, and reliability as part of everyday work. It also brings risks, such as too many dependencies between teams, releasing things before they are truly ready, or allowing many small changes to slowly create larger performance costs over time.",
                "What makes this article especially useful is that it treats deployment as both a technical and human challenge. It is not only about pipelines and tools, but also about trust, responsibility, and learning quickly from real results. That is what gives the article its lasting value for anyone trying to understand how modern software teams deliver changes safely and steadily.",
            ],
        },
    },
}
