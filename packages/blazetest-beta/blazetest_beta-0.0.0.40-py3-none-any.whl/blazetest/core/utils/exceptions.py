class ConfigurationValidationException(Exception):
    pass


class AWSRegionNotFound(Exception):
    pass


class ConfigurationFileNotFound(Exception):
    pass


class ConfigurationMissingValue(Exception):
    pass


class S3BucketNotFound(Exception):
    pass


class LambdaNotCreated(Exception):
    pass


class LicenseNotSpecified(Exception):
    pass


class LicenseNotValid(Exception):
    pass


class LicenseExpired(Exception):
    pass


class CommandExecutionException(Exception):
    pass


class UnsupportedInfraSetupTool(Exception):
    pass
