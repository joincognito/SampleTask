import asyncio


COMPANIES_SAMPLE_CSV = "companies_sample.csv"


async def company_employs_sdrs(company_name: str, company_website: str) -> bool:
    # TODO: code this function.
    #  Hint: use google search to find people at the company with the title similiar to "Sales Development Representative" or "SDR" that work at the company.
    pass


async def company_is_hiring_sdrs(company_name: str, company_website: str) -> bool:
    # TODO: code this function.
    # Check the careers page of the company website to see if open positions for sale development representatives (SDRs) exist.
    pass


async def main():
    # TODO: code this function.

    # TODO: read the samples companies from the given CSV file

    # TODO: for each company, check if it employs SDRs and if it is hiring SDRs

    # TODO: save the results to a CSV file "sample_copmanies_enriched.csv"
    pass


if __name__ == "__main__":
    asyncio.run(main())
