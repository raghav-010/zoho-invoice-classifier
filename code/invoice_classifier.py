"""
Zoho Books Invoice Classifier

Description:
    A Zoho Books Custom Function that automatically classifies invoices
    into customer tiers based on the invoice total.

    This is not a high level code however i just creted this to understand and revise Python and instead of writing the code on VS code or Pycharm
    I just used Zoho Books so that I can know what are all the limitations and scenarios that I can use on a third-party application.
    Please check out this code if you like.

Trigger:
    Invoice Status → Sent

Classification Rules:
    - Enterprise : Amount >= 5000
    - High       : Amount >= 1000
    - Medium     : Amount >= 500
    - Low        : Amount < 500

Code written by:
    Raghav 
"""

import json


def runner(context, basicIO):
    """
    # This is the starting point of custom function I don't want this to be like Ai prompt so I have just given the comments on my own.
    """

    try:
        context.log.INFO("=== Invoice Classification Started ===")

        # Read invoice data from the workflow input
        invoice = json.loads(basicIO.getParameter("invoice"))

        invoice_number = invoice.get("invoice_number", "")
        customer_name = invoice.get("customer_name", "")
        total_amount = float(invoice.get("total", "0"))

        context.log.INFO(f"Invoice Number : {invoice_number}")
        context.log.INFO(f"Customer       : {customer_name}")
        context.log.INFO(f"Invoice Amount : {total_amount}")

        # Find the customer tier
        if total_amount >= 5000:
            tier = "Enterprise"
        elif total_amount >= 1000:
            tier = "High"
        elif total_amount >= 500:
            tier = "Medium"
        else:
            tier = "Low"

        context.log.INFO(f"Classification : {tier}")
        context.log.INFO(
            f"Invoice {invoice_number} classified successfully as {tier} tier."
        )

        context.log.INFO("===== Execution Completed Successfully =====")

    except Exception as error:
        context.log.INFO(f"Execution Failed: {error}")
