"""Module for nude.protocol.str"""

class FailedConstraint(Exception):
    """Class for FailedConstraint Exception, raised when a constraint fails"""

class ConstraintDefinitionError(Exception):
    """Class for ConstraintDefinitionError Exception, raised when a constraint
    value in the protocol is incorrect"""

class Type:
    """Type for nude.protocol.str"""
    def __init__(self, component):
        self.component = component
        self.constraints = []

        for key, expects in component.items():
            if key.endswith('?'):
                constraint = key
                tag = "schema_{constraint}".format(constraint=constraint[:-1])

                schema = getattr(self, tag)
                schema(expects)

                self.constraints.append(constraint)

    @staticmethod
    def schema_uppercase(expects):
        """Raises ConstraintDefinitionError if expects is not a bool"""
        if not isinstance(expects, bool):
            raise ConstraintDefinitionError("'uppercase?' is not a bool")

    def validate(self, value):
        """Iterates over each of the constraints for this object and
        ensures value conforms to eacb of them"""
        errors = []
        for constraint in self.constraints:
            tag = "validate_{constraint}".format(constraint=constraint[:-1])
            validator = getattr(self, tag)

            expects = self.component[constraint]

            try:
                validator(value, expects)
            except FailedConstraint as exception:
                errors.append(str(exception))

        return errors

    @staticmethod
    def validate_uppercase(value, expects):
        """Raises FailedConstraint if value.isupper is not as expected"""
        if value.isupper() != expects:
            failure = "not uppercase"
            if not expects:
                failure = "uppercase"

            message = "'{value}' is {failure}".format(value=value, failure=failure)
            raise FailedConstraint(message)
