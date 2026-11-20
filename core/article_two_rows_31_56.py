"""Article 2 horizontal timeline rows 31–56 (verbatim description text; dates year-month)."""


def article_two_rows_31_56():
    return [
        {
            "date": "2016-11",
            "title": "AWS SAM",
            "description": (
                "Serverless applications on AWS could quickly become hard to define because teams still had to describe many related cloud resources in detail. AWS SAM solved this by adding a simpler model on top of CloudFormation for Lambda functions, APIs, and related serverless resources. It made serverless applications easier to define, review, and deploy as one unit. Example: Before: a team writes large CloudFormation files for each Lambda and API. After: it defines the serverless app in a shorter SAM template."
            ),
            "image": "img/solutions logs/31. AWS SAM.png",
            "image_alt": "AWS SAM placeholder graphic",
            "side": "left",
            "connector_color": "rgba(64, 224, 208, 0.88)",
        },
        {
            "date": "2016-12",
            "title": "AWS CodeBuild",
            "description": (
                "Build servers often required maintenance, scaling work, and manual setup of build environments. AWS CodeBuild solved this by giving teams a managed build service that could compile code, run tests, and produce artifacts without operating the build infrastructure themselves. Example: Before: a team maintains its own build VM and updates tools manually. After: CodeBuild starts clean builds on demand."
            ),
            "image": "img/solutions logs/32. AWS CodeBuild.png",
            "image_alt": "AWS CodeBuild placeholder graphic",
            "side": "right",
            "connector_color": "rgba(255, 107, 138, 0.88)",
        },
        {
            "date": "2017-01",
            "title": "Flux CD",
            "description": (
                "Kubernetes clusters often drifted away from the configuration stored in Git because deployments were still triggered or changed manually. Flux CD solved this by continuously reconciling cluster state with what was declared in version control. That made deployments more auditable and reduced configuration drift. Example: Before: someone changes the cluster manually and Git no longer matches. After: Flux detects drift and restores the Git state."
            ),
            "image": "img/solutions logs/33. Flux CD.png",
            "image_alt": "Flux CD placeholder graphic",
            "side": "left",
            "connector_color": "rgba(125, 211, 252, 0.9)",
        },
        {
            "date": "2017-04",
            "title": "Packer 1.0",
            "description": (
                "Teams often built machine images by hand, which made base images inconsistent and difficult to reproduce. Packer solved this by letting teams create images for different platforms from one source configuration. That made image creation more repeatable and improved consistency across environments. Example: Before: engineers build AMIs manually with different package versions. After: Packer creates matching images from one definition."
            ),
            "image": "img/solutions logs/34. Packer 1.0.png",
            "image_alt": "Packer 1.0 placeholder graphic",
            "side": "right",
            "connector_color": "rgba(251, 191, 36, 0.9)",
        },
        {
            "date": "2017-05",
            "title": "Istio",
            "description": (
                "In microservice systems, concerns like service-to-service security, traffic control, and telemetry were often implemented separately inside each service. Istio solved this by introducing a service mesh that moved those concerns into a shared infrastructure layer. That made distributed systems easier to observe, secure, and control consistently. Example: Before: each service adds its own retries and traffic logic. After: Istio applies those rules from the mesh layer."
            ),
            "image": "img/solutions logs/35. Istio.png",
            "image_alt": "Istio placeholder graphic",
            "side": "left",
            "connector_color": "rgba(239, 68, 68, 0.88)",
        },
        {
            "date": "2017-08",
            "title": "GitOps model",
            "description": (
                "Infrastructure and deployment changes were often hard to audit because they happened through dashboards, scripts, or direct cluster access. The GitOps model solved this by making Git the source of truth for desired system state and using automation to apply those changes. That improved reviewability, traceability, and rollback. Example: Before: a production setting is changed directly in the cluster. After: the change goes through Git and is applied automatically."
            ),
            "image": "img/solutions logs/36. GitOps model.png",
            "image_alt": "GitOps model placeholder graphic",
            "side": "right",
            "connector_color": "rgba(59, 130, 246, 0.88)",
        },
        {
            "date": "2017-12",
            "title": "Fluentd 1.0",
            "description": (
                "Logs from applications and infrastructure were often scattered across different systems and formats, making centralized analysis difficult. Fluentd solved this by acting as a common data collector that could gather, transform, and route logs to multiple destinations. That made logging pipelines more consistent and portable. Example: Before: each app writes logs to different files and tools. After: Fluentd collects and forwards them into one pipeline."
            ),
            "image": "img/solutions logs/37. Fluentd 1.0.png",
            "image_alt": "Fluentd 1.0 placeholder graphic",
            "side": "left",
            "connector_color": "rgba(34, 211, 238, 0.88)",
        },
        {
            "date": "2018-04",
            "title": "Cilium",
            "description": (
                "Traditional container networking and security often depended on older Linux mechanisms that became harder to scale and manage in dynamic Kubernetes environments. Cilium solved this by using eBPF-based networking and security controls designed for modern container systems. That improved visibility, policy control, and performance. Example: Before: network rules rely on large iptables chains. After: Cilium enforces policy with eBPF in the kernel."
            ),
            "image": "img/solutions logs/38. Cilium.png",
            "image_alt": "Cilium placeholder graphic",
            "side": "right",
            "connector_color": "rgba(16, 185, 129, 0.88)",
        },
        {
            "date": "2018-05",
            "title": "Kustomize",
            "description": (
                "Kubernetes teams often copied and edited many YAML files for each environment, which created duplication and maintenance problems. Kustomize solved this by letting teams customize base configurations through overlays without templating the original files. That made environment-specific changes easier to manage. Example: Before: dev and prod keep separate copies of almost the same YAML. After: both reuse one base with small overlays."
            ),
            "image": "img/solutions logs/39. Kustomize.png",
            "image_alt": "Kustomize placeholder graphic",
            "side": "left",
            "connector_color": "rgba(236, 72, 153, 0.88)",
        },
        {
            "date": "2018-06",
            "title": "Pulumi",
            "description": (
                "Infrastructure as code tools were powerful, but some teams found purely declarative syntax limiting when they needed richer logic and reusable abstractions. Pulumi solved this by letting infrastructure be defined with general-purpose programming languages. That made it easier to apply software engineering patterns to cloud infrastructure. Example: Before: shared infrastructure logic is awkward in plain templates. After: Pulumi lets teams build reusable components in code."
            ),
            "image": "img/solutions logs/40. Pulumi.png",
            "image_alt": "Pulumi placeholder graphic",
            "side": "right",
            "connector_color": "rgba(20, 184, 166, 0.9)",
        },
        {
            "date": "2018-07",
            "title": "Knative",
            "description": (
                "Teams wanted serverless behavior on Kubernetes, but Kubernetes alone did not provide a complete set of building blocks for event-driven workloads and request-based autoscaling. Knative solved this by adding serverless-oriented components on top of Kubernetes. That made it easier to run event-driven and autoscaling workloads while staying in the Kubernetes ecosystem. Example: Before: a team assembles autoscaling and event routing by itself. After: Knative provides those building blocks on Kubernetes."
            ),
            "image": "img/solutions logs/41. Knative.png",
            "image_alt": "Knative placeholder graphic",
            "side": "left",
            "connector_color": "rgba(96, 165, 250, 0.9)",
        },
        {
            "date": "2018-09",
            "title": "Azure DevOps",
            "description": (
                "Planning, source control, pipelines, packages, and testing were often spread across multiple Microsoft-branded services and product names. Azure DevOps solved this by bringing those capabilities together under one clearer DevOps platform brand and service family. That made delivery workflows more unified for Microsoft-centered teams. Example: Before: a team jumps between separate Microsoft tools and names. After: it uses Azure DevOps for boards, repos, pipelines, and artifacts."
            ),
            "image": "img/solutions logs/42. Azure DevOps.png",
            "image_alt": "Azure DevOps placeholder graphic",
            "side": "right",
            "connector_color": "rgba(245, 158, 11, 0.9)",
            "position_pct_nudge": -1.0,
            "marker_translate_x_px": 20,
        },
        {
            "date": "2018-09",
            "title": "Linkerd 2.0",
            "description": (
                "Service meshes could add significant complexity and resource overhead, which made adoption harder for some teams. Linkerd 2.0 solved this by focusing on a lighter, simpler service mesh for Kubernetes with strong performance and lower operational complexity. Example: Before: the team avoids service mesh because it feels too heavy. After: Linkerd 2.0 adds mTLS and observability with less overhead."
            ),
            "image": "img/solutions logs/43. Linkerd 2.0.png",
            "image_alt": "Linkerd 2.0 placeholder graphic",
            "side": "left",
            "connector_color": "rgba(248, 113, 113, 0.88)",
            "position_pct_nudge": 1.05,
            "marker_translate_x_px": -15,
            "marker_translate_y_delta_px": 15,
        },
        {
            "date": "2018-10",
            "title": "GitHub Actions",
            "description": (
                "Workflow automation often required external CI systems even when the code already lived on GitHub. GitHub Actions solved this by bringing workflow automation directly into the GitHub platform, letting teams build, test, package, and deploy from repository events. Example: Before: every workflow depends on an external CI tool. After: GitHub Actions runs from repository events inside GitHub."
            ),
            "image": "img/solutions logs/44. GitHub Actions.png",
            "image_alt": "GitHub Actions placeholder graphic",
            "side": "right",
            "connector_color": "rgba(129, 140, 248, 0.88)",
        },
        {
            "date": "2018-11",
            "title": "Firecracker",
            "description": (
                "Containers were fast and efficient, but some workloads needed stronger isolation closer to virtual machines without the full weight of traditional VMs. Firecracker solved this by introducing lightweight microVMs designed for serverless and container-based services. That improved the balance between speed and isolation. Example: Before: a team chooses between fast containers and heavier VMs. After: Firecracker provides lightweight microVMs with stronger isolation."
            ),
            "image": "img/solutions logs/45. Firecracker.png",
            "image_alt": "Firecracker placeholder graphic",
            "side": "left",
            "connector_color": "rgba(64, 224, 208, 0.88)",
        },
        {
            "date": "2019-03",
            "title": "Tekton",
            "description": (
                "CI/CD tools often felt separate from Kubernetes even when teams were already operating their applications there. Tekton solved this by defining pipelines and build tasks as Kubernetes-native resources. That made software delivery workflows fit more naturally into cloud-native environments. Example: Before: apps run on Kubernetes but the pipeline lives elsewhere. After: Tekton runs the pipeline as Kubernetes-native resources."
            ),
            "image": "img/solutions logs/46. Tekton.png",
            "image_alt": "Tekton placeholder graphic",
            "side": "right",
            "connector_color": "rgba(255, 107, 138, 0.88)",
        },
        {
            "date": "2019-05",
            "title": "OpenTelemetry",
            "description": (
                "Observability tooling had become fragmented, with separate standards and libraries for traces, metrics, and instrumentation. OpenTelemetry solved this by unifying telemetry collection and instrumentation under one open framework. That improved portability and reduced duplication across observability tooling. Example: Before: tracing and metrics use different libraries and rules. After: OpenTelemetry gives one common instrumentation approach."
            ),
            "image": "img/solutions logs/47. OpenTelemetry.png",
            "image_alt": "OpenTelemetry placeholder graphic",
            "side": "left",
            "connector_color": "rgba(125, 211, 252, 0.9)",
            "position_pct_nudge": -1.0,
            "marker_translate_x_px": 20,
        },
        {
            "date": "2019-05",
            "title": "Argo CD",
            "description": (
                "Kubernetes deployments were often still driven by imperative commands, which made changes harder to audit and cluster state harder to keep aligned with Git. Argo CD solved this by providing a GitOps-focused continuous delivery controller for Kubernetes. It continuously compared live state with the desired state in Git and could sync the cluster back when drift appeared. Example: Before: a release engineer runs kubectl manually. After: Argo CD syncs the cluster from Git automatically."
            ),
            "image": "img/solutions logs/48. Argo CD.png",
            "image_alt": "Argo CD placeholder graphic",
            "side": "right",
            "connector_color": "rgba(251, 191, 36, 0.9)",
            "position_pct_nudge": 1.05,
        },
        {
            "date": "2020-03",
            "title": "Backstage",
            "description": (
                "As engineering organizations grew, developers often had to jump across many tools to find service ownership, documentation, deployments, and operational context. Backstage solved this by creating a unified internal developer portal. That reduced fragmentation and improved the developer experience around internal systems. Example: Before: docs, owners, and deploy links are scattered across tools. After: Backstage shows them in one portal."
            ),
            "image": "img/solutions logs/49. Backstage.png",
            "image_alt": "Backstage placeholder graphic",
            "side": "left",
            "connector_color": "rgba(239, 68, 68, 0.88)",
        },
        {
            "date": "2020-12",
            "title": "Crossplane",
            "description": (
                "Platform teams often wanted to offer self-service cloud infrastructure, but the management model for cloud resources was still spread across provider-specific tools and templates. Crossplane solved this by extending Kubernetes so teams could manage cloud resources and build reusable platform APIs from one control plane model. Example: Before: developers request databases and networks through separate cloud tools. After: Crossplane exposes them as platform APIs from Kubernetes."
            ),
            "image": "img/solutions logs/50. Crossplane.png",
            "image_alt": "Crossplane placeholder graphic",
            "side": "right",
            "connector_color": "rgba(59, 130, 246, 0.88)",
        },
        {
            "date": "2021-01",
            "title": "Telepresence 2",
            "description": (
                "Developing one microservice in a large Kubernetes application could be slow because reproducing the full remote environment locally was difficult. Telepresence 2 solved this by letting developers connect a local service into a remote cluster and test against real dependent services. That shortened feedback loops for cloud-native development. Example: Before: a developer runs many dependent services locally to test one change. After: Telepresence connects the local service to the remote cluster."
            ),
            "image": "img/solutions logs/51. Telepresence 2.png",
            "image_alt": "Telepresence 2 placeholder graphic",
            "side": "left",
            "connector_color": "rgba(34, 211, 238, 0.88)",
        },
        {
            "date": "2021-02",
            "title": "Cosign",
            "description": (
                "Signing and verifying software artifacts, especially container images, was often too difficult for normal development workflows. Cosign solved this by making signing and verification much easier for OCI artifacts. That helped teams improve software supply chain trust with less operational overhead. Example: Before: a team publishes container images without easy verification. After: Cosign signs the image and users verify its origin."
            ),
            "image": "img/solutions logs/52. Cosign.png",
            "image_alt": "Cosign placeholder graphic",
            "side": "right",
            "connector_color": "rgba(16, 185, 129, 0.88)",
        },
        {
            "date": "2022-06",
            "title": "HTTP/3",
            "description": (
                "HTTP/2 improved performance, but it still inherited some transport-level limitations from TCP, especially around head-of-line blocking. HTTP/3 solved this by mapping HTTP onto QUIC, which improved connection behavior and performance on modern networks. Example: Before: packet loss on one TCP stream delays other traffic. After: HTTP/3 uses QUIC streams to reduce that blocking."
            ),
            "image": "img/solutions logs/53. HTTP3.png",
            "image_alt": "HTTP/3 placeholder graphic",
            "side": "left",
            "connector_color": "rgba(236, 72, 153, 0.88)",
        },
        {
            "date": "2022-09",
            "title": "Istio Ambient Mesh",
            "description": (
                "Traditional service meshes usually depended on sidecar proxies for each workload, which increased resource use and operational complexity. Istio Ambient Mesh solved this by introducing a sidecar-less data plane mode designed for simpler operations and lower overhead while preserving core mesh capabilities. Example: Before: every pod runs its own sidecar proxy. After: ambient mesh moves much of that work to shared infrastructure."
            ),
            "image": "img/solutions logs/54. Istio Ambient Mesh.png",
            "image_alt": "Istio Ambient Mesh placeholder graphic",
            "side": "right",
            "connector_color": "rgba(20, 184, 166, 0.9)",
        },
        {
            "date": "2022-10",
            "title": "Sigstore GA",
            "description": (
                "Software signing infrastructure was often difficult to operate and too costly for many open-source and smaller teams. Sigstore GA solved this by making a stable, community-operated signing and verification service broadly available. That lowered the barrier to stronger software supply chain security. Example: Before: many projects ship artifacts without an easy public signing flow. After: Sigstore offers production-grade public signing and verification services."
            ),
            "image": "img/solutions logs/55. Sigstore GA.png",
            "image_alt": "Sigstore GA placeholder graphic",
            "side": "left",
            "connector_color": "rgba(96, 165, 250, 0.9)",
        },
        {
            "date": "2023-07",
            "title": "Flux 2 GA",
            "description": (
                "Early GitOps setups could work well, but teams still wanted a more mature and stable production-ready set of GitOps components. Flux 2 GA solved this by marking the Flux 2 component model as generally available. That gave teams a stronger foundation for production GitOps operations on Kubernetes. Example: Before: teams see Flux 2 as still evolving for core production use. After: Flux 2 GA becomes a stable GitOps baseline."
            ),
            "image": "img/solutions logs/56. Flux 2 GA.png",
            "image_alt": "Flux 2 GA placeholder graphic",
            "side": "right",
            "connector_color": "rgba(245, 158, 11, 0.9)",
        },
    ]
