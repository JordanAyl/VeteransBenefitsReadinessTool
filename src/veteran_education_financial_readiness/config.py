
# config.py

from models import AnnualRatesConfig

# Demo values, tweak these to match the real VA tables.
DEFAULT_ANNUAL_RATES = AnnualRatesConfig(
    year_label="2025-2026",
    private_foreign_tuition_cap_year=29000.0,  # example national cap
    books_cap_year=1000.0,                      # approx full-year books cap
    per_credit_books_full=41.67,                # ~ $1000 / 24 credits
    terms_per_year=2,                           # 2 semesters per year
)


# BAH / MHA basis for Post-9/11 GI Bill: see `bah_rates_2026_data.py`
# (2026 rates, E-5 with dependents) and location picker in `app.py`.