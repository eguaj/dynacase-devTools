import argparse

import generateFamily
import generateInfoXml
import generateWorkflow
import addApplication
import extractAttrProductConst

def createParser():
    mainParser = argparse.ArgumentParser(prog="Dynacase DevTools", description="Tools to facilitate dev")
    subparsers = mainParser.add_subparsers(help="sub-command help")

    parserInfoXml = subparsers.add_parser("generateInfoXml", help="Generate info.xml file from targets. (requires PyXML)")
    generateInfoXml.defineParseArguments(parserInfoXml)
    parserInfoXml.set_defaults(func=generateInfoXml.executeInfoXml)

    parserGenerateFamily = subparsers.add_parser("generateFamily", help="Generate Family files.")
    generateFamily.defineParseArguments(parserGenerateFamily)
    parserGenerateFamily.set_defaults(func=generateFamily.executeGenerateFamily)

    parserGenerateWorkflow = subparsers.add_parser("generateWorkflow", help="Generate workflow.")
    generateWorkflow.defineParseArguments(parserGenerateWorkflow)
    parserGenerateWorkflow.set_defaults(func=generateWorkflow.executeGenerateWorkflow)

    parserAddApplication = subparsers.add_parser("addApplication", help="Add a new application in current module")
    addApplication.defineParseArguments(parserAddApplication)
    parserAddApplication.set_defaults(func=addApplication.executeAddApplication)

    parserExtractAttr = subparsers.add_parser("extractAttrProductConst", help="Inserts constants for attributes and parameters in Method files.")
    extractAttrProductConst.defineParseArguments(parserExtractAttr)
    parserExtractAttr.set_defaults(func=extractAttrProductConst.executeExtractAttr)

    return mainParser


def main():
    argParser = createParser()
    args = argParser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()