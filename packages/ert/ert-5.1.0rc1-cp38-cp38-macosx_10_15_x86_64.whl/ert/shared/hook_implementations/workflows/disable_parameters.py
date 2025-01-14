from ert import ErtScript


class DisableParametersUpdate(ErtScript):
    """The DISABLE_PARAMETERS workflow disables parameters,
    so they are excluded from the update step. The job takes a group
    of parameters as input:

    DISABLE_PARAMETERS DISABLE_PRED

    The parameters that are given as arguments will be removed from the
    update.

    Note that unknown parameter names will be silently ignored.

    This workflow is recommended to be run as a PRE_FIRST_UPDATE hook.

    An example to disable parameters in three steps follows.

    First, in the ert config file, include:

        LOAD_WORKFLOW disable_parameter_pred
        HOOK_WORKFLOW disable_parameter_pred PRE_FIRST_UPDATE

        GEN_KW DISABLE_PRED pred.tmpl pred.json pred_priors
        GEN_KW COEFFS coeff.tmpl coeffs.json coeff_priors

    The content of "coeff_priors" could be for example:

        COEFF_A UNIFORM 0 1
        COEFF_B UNIFORM 0 2
        COEFF_C UNIFORM 0 5

    And the content of "pred_priors":

        COEFF_D UNIFORM 1 3
        COEFF_E UNIFORM 5 9

    Second, make a new file called "disable_parameter_pred" with:

        DISABLE_PARAMETERS DISABLE_PRED

    Finally, after running the ert config file, the user can check the plots
    (e.g. in the gui click "Create plots") that the disabled parameters were not
    updated. For the example above, there would be two groups of parameters:

        COEFFS:COEFF_A
        COEFFS:COEFF_B
        COEFFS:COEFF_C

        DISABLE_PRED:COEFF_D
        DISABLE_PRED:COEFF_E

    All the parameters in the COEFFS group are updated from one iteration to the next,
    e.g. the standard deviation or/and distribution of the parameters are updated.
    At the same time, the parameters in the DISABLE_PRED group are not updated and they
    have the same distribution and sampling in all iterations and realizations.
    """

    def run(self, disable_parameters):  # pylint: disable=arguments-differ
        ert = self.ert()
        disable_parameters = disable_parameters.split(",")
        disable_parameters = [val.strip() for val in disable_parameters]
        altered_update_step = [
            {
                "name": "DISABLED_PARAMETERS",
                "observations": ert._observation_keys,
                "parameters": [
                    key for key in ert._parameter_keys if key not in disable_parameters
                ],
            }
        ]
        ert.update_configuration = altered_update_step
