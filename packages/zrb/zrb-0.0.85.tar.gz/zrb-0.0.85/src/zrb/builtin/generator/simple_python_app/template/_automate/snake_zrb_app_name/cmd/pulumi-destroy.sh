(pulumi stack select {{input.snake_zrb_app_name_pulumi_stack}} || pulumi stack init {{input.snake_zrb_app_name_pulumi_stack}})
pulumi destroy --skip-preview