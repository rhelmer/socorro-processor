from ujson import dumps

from socorro_processor.processor_2015 import Processor2015

#------------------------------------------------------------------------------
# these are the steps that define processing a crash at Mozilla.
# they are used to define the default rule configuration for the Mozilla
# crash processor based on Procesor2015

mozilla_processor_rule_sets = [
    [   # rules to change the internals of the raw crash
        "raw_transform",
        "processor.json_rewrite",
        "socorro.lib.transform_rules.TransformRuleSystem",
        "apply_all_rules",
        "socorro_processor.mozilla_transform_rules.ProductRewrite,"
        "socorro_processor.mozilla_transform_rules.ESRVersionRewrite,"
        "socorro_processor.mozilla_transform_rules.PluginContentURL,"
        "socorro_processor.mozilla_transform_rules.PluginUserComment,"
        "socorro_processor.mozilla_transform_rules.WebAppRuntime"

    ],
    [   # rules to transform a raw crash into a processed crash
        "raw_to_processed_transform",
        "processer.raw_to_processed",
        "socorro.lib.transform_rules.TransformRuleSystem",
        "apply_all_rules",
        "socorro_processor.general_transform_rules.IdentifierRule, "
        "socorro_processor.breakpad_transform_rules.BreakpadStackwalkerRule, "
        "socorro_processor.mozilla_transform_rules.ProductRule, "
        "socorro_processor.mozilla_transform_rules.UserDataRule, "
        "socorro_processor.mozilla_transform_rules.EnvironmentRule, "
        "socorro_processor.mozilla_transform_rules.PluginRule, "
        "socorro_processor.mozilla_transform_rules.AddonsRule, "
        "socorro_processor.mozilla_transform_rules.DatesAndTimesRule, "
        "socorro_processor.mozilla_transform_rules.OutOfMemoryBinaryRule, "
        "socorro_processor.mozilla_transform_rules.JavaProcessRule, "
        "socorro_processor.mozilla_transform_rules.Winsock_LSPRule, "
    ],
    [   # post processing of the processed crash
        "processed_transform",
        "processer.processed",
        "socorro.lib.transform_rules.TransformRuleSystem",
        "apply_all_rules",
        "socorro_processor.breakpad_transform_rules.CrashingThreadRule, "
        "socorro_processor.general_transform_rules.CPUInfoRule, "
        "socorro_processor.general_transform_rules.OSInfoRule, "
        "socorro_processor.mozilla_transform_rules.ExploitablityRule, "
        "socorro_processor.mozilla_transform_rules.FlashVersionRule, "
        "socorro_processor.mozilla_transform_rules.TopMostFilesRule, "
        "socorro_processor.mozilla_transform_rules.MissingSymbolsRule, "
        "socorro_processor.signature_utilities.SignatureGenerationRule,"
        "socorro_processor.signature_utilities.StackwalkerErrorSignatureRule, "
        "socorro_processor.signature_utilities.OOMSignature, "
        "socorro_processor.signature_utilities.SigTrunc, "
        "socorro_processor.signature_utilities.SignatureRunWatchDog, "
    ],
    [   # a set of classifiers for support
        "support_classifiers",
        "processor.support_classifiers",
        "socorro.lib.transform_rules.TransformRuleSystem",
        "apply_until_action_succeeds",
        "socorro_processor.support_classifiers.BitguardClassifier, "
        "socorro_processor.support_classifiers.OutOfDateClassifier"
    ],
    [   # a set of special request classifiers
        "skunk_classifiers",
        "processor.skunk_classifiers",
        "socorro.lib.transform_rules.TransformRuleSystem",
        "apply_until_action_succeeds",
        "socorro_processor.skunk_classifiers.DontConsiderTheseFilter, "
        # currently not in use, anticipated to be re-enabled in the future
        #"socorro_processor.skunk_classifiers.UpdateWindowAttributes, "
        "socorro_processor.skunk_classifiers.SetWindowPos, "
        # currently not in use, anticipated to be re-enabled in the future
        #"socorro_processor.skunk_classifiers.SendWaitReceivePort, "
        # currently not in use, anticipated to be re-enabled in the future
        #"socorro_processor.skunk_classifiers.Bug811804, "
        # currently not in use, anticipated to be re-enabled in the future
        #"socorro_processor.skunk_classifiers.Bug812318, "
        "socorro_processor.skunk_classifiers.NullClassification"
    ]
]


#==============================================================================
class MozillaProcessorAlgorithm2015(Processor2015):
    """this is the class that processor uses to transform """

    Processor2015.required_config.rule_sets.set_default(
        dumps(mozilla_processor_rule_sets),
        force=True
    )

