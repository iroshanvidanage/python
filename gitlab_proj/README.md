# Readme file for GitLab project

## Developing a Pyhton Web App using Flask

### Gitlab

- Has a image registry and the following uri can be found in the $CI_REGISTRY_IMAGE

- `registry.gitlab.com/[user_name]/[project_name]`
    - `/[image_name]:[tags]`

- image name can have up to three levels
    - `/[image_name]/[image_name]:[tags]`
    - `/[image_name]/[image_name]/[image_name]:[tags]`

- An access token should be passed to access the registry and should have minimum access for read & write
    - `read_registry` for read (pull) access
    - `write_redistry` for write (push) access


### Heroku

- Pushing the image to Heroku containers

- There's a registry in Heroku
    - `registry.heroku.com/[app_in_heroku]/[process_type]`

- Need a heroku token from API key and store it as a secret variable in gitlab `HEROKU_STAGING_API_KEY`

### Procfile

- Procfile is used declare the process types to specifies the commands that are executed by the app on start up included in the Heroku Apps.


### Dynamic environments

- In order to stop a dynamic environment, need to remove the protection from the `feature-` branches and secrets/variables.
- To the stop environment to be worked, need to create a merge request with Delete source branch option applied.

- The following is used to stop the git checkout the code.
- The GitLab runner will always try to checkout the code once a job is complete, since the code branch will be deleted in the sceneario, we need to stop it from checking out the code.

```yml
variables:
    GIT_STRATEGY: none
```

### Job Templating

- Move similar jobs to a template and import them when necessary.

- YAML Anchors

```yml
---
# this file only contains example jobs used for yaml anchors

.job_template: &template # & shows that this is an anchor and the name of the anchor is `template`
  image: python:3.8.0-slim
  before-script:
    - pip3 install -r requirements.txt
  only:
    - main


job_1:
  <<: *template # <<: indicates that the lines from the anchor should be merged to this mapping.
  stage: test
  script:
    - echo "Job_1 starts"
    - echo "Job_1 ends !"


job_2:
  <<: *template # the anchor is referenced from the * (star)
  stage: test
  script:
    - echo "Job_2 starts"
    - echo "Job_2 ends !"
```

- Generalized Job variables should be defined for each job or environment. (locally in the job or in the pipeline's CI/CD variables)

```yml

# these can be declared for each environment in the CI/CD variables in the project settings
# feature, staging, production

job:
  variables:
    APP:
    HEROKU:
    HEROKU_API_KEY:
```