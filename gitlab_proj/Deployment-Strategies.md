# Deployment Strategies

- The practices to change or upgrade an application. It defines how you want to deliver your software (product).

- Types:
    - Recreate Deployment
    - Blue - Green Deployment
    - Canary Deployment
    - A/B Testing

- Choosing a strtegy depends on the business model.


## Recreate Deployment

- Most basic form of deployment.
- Existing application is scaled down (stopped) and the new version is scaled up (started).
- Not using the load balancer feature where the application availability is not an issue.
- Used where the service is not a business, mission or revenue critical and only concern is deployment cost.

- Pros:
    - Very simple and fast.
    - Cheaper - no extra infra cost.
    - No need to manage multiple versions in parallel

- Cons:
    - Riskiest practice.
    - Involves downtime during deployment.
    - Application is inaccessible during downtime.


## Blue - Green Deployment

- A.k.a Red/Black deployments, performing two identical deployments. The Blue - current stable version while Green is the new version.
- The new version is deployed parallely and the load-balancer will re-route the traffic to the new versions.

- Pros:
    - Zero downtime.
    - Instant Rollback.

- Cons:
    - Increased operational overhead and cost.


## Canary Deployment

- It's a Blue/Green deployment, but it is more risk-aversed and more phase approached.
- This is where the only a portion of the traffic is routed initally to the new version and gradually rolling out the product.

- Pros:
    - Lowest risk-prone.
    - Ability to test live production traffic.
    - Zero downtime.

- Cons:
    - Scripting the release can be complex. Involves additional research.
    - Slow rollout.


## A/B Testing

- A/B testing deployment starategy relies on real-world statistical data to decide on a rollout or rollback as it focusses on gauging user acceptance of new application features.
- Primarily focussed on experimentation and exploration.

- Pros:
    - Best choice when you want to make release decisions with the real-world statistical data.

- Cons:
    - Involves the experimental nature where it can breaks the application, service or ux.
    - Scripting the release can be complex.
