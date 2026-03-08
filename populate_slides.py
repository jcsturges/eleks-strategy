"""
Populate the Antigravity (ELEKS AG) executive overview Google Slides deck.
Presentation ID: 1jRmADg5SJSLKxAWJOHQdAh9LIPhxSj6NqRx31xArhUY
"""
import pickle
from googleapiclient.discovery import build

PRESENTATION_ID = "18eEyVvIzyVqOsGLaum8RqwV7HHbCGNmHCeLnDqTjEsg"
TOKEN_PATH = "/Users/james/.config/gw-mcp/token.pickle"

SLIDE_CONTENT = [
    {
        "title": "Antigravity (ELEKS AG)",
        "body": (
            "Building the Premier Agentic AI Advisory Practice in the US Market\n\n"
            "Confidential  |  Executive Overview  |  March 2026"
        ),
    },
    {
        "title": "Why Now? The Agentic AI Advisory Gap",
        "body": (
            "THE MARKET MOMENT\n"
            "• Agentic AI is a greenfield category — no established advisory leader\n"
            "• Enterprise buyers need strategic guidance: WHERE and HOW to deploy agents\n"
            "• Failed AI pilots are mounting; enterprises need strategy, not more tools\n"
            "• Advisory spend on AI strategy is growing 3× faster than implementation spend\n\n"
            "ELEKS' UNFAIR ADVANTAGE\n"
            "• 34 years of engineering excellence  |  2,100+ employees  |  $120M revenue\n"
            "• 100+ data scientists in R&D lab; 200+ data engineers\n"
            "• MLOps/LLMOps capabilities already in production\n"
            "• AWS Advanced, Microsoft Solutions, Snowflake & Databricks partnerships\n"
            "• Deep expertise: Financial Services, Healthcare, Energy, Government\n\n"
            "THE GAP: ELEKS can BUILD. Enterprises need someone to help them DECIDE."
        ),
    },
    {
        "title": "The Case for a New Brand — Not a Rebrand",
        "body": (
            "THE ELEKS BRAND PROBLEM\n"
            "• 34 years = \"offshore engineering execution\" in buyer minds\n"
            "• CIOs/CTOs hire McKinsey, BCG, Deloitte for strategy — not IT services firms\n"
            "• Rate ceiling: Impossible to charge $250–500/hr under the offshore brand\n"
            "• Top US-based consultants won't join a \"Ukrainian outsourcer\"\n\n"
            "WHAT A SEPARATE BRAND UNLOCKS\n"
            "• Premium advisory positioning from Day 1 (value pricing, not T&M)\n"
            "• C-suite buyer credibility — peer-to-peer with CIO/CTO/CDO\n"
            "• Talent magnet for senior US-based consultants\n"
            "• Clean engagement model: New brand advises → ELEKS implements\n"
            "• Risk isolation: If it fails, ELEKS brand is completely unaffected\n\n"
            "SUCCESSFUL ANALOGUES: BCG Platinion  |  Slalom Build  |  Bain Bridgespan\n\n"
            "New Brand: $150–500/hr  |  40–50% EBITDA margin  |  C-suite buyer\n"
            "ELEKS:     $75–150/hr   |  20–25% EBITDA margin  |  VP/Director buyer"
        ),
    },
    {
        "title": "Antigravity: Service Portfolio",
        "body": (
            "TIER 1 — ADVISORY  (Antigravity Exclusive)\n"
            "  • Agentic AI Readiness Assessment ........... $75K – $150K\n"
            "  • Agentic AI Strategy & Roadmap ............. $150K – $300K\n"
            "  • Data & AI Platform Strategy ............... $100K – $200K\n"
            "  • AI Governance & Operating Model ........... $100K – $250K\n\n"
            "TIER 2 — IMPLEMENTATION  (Antigravity Advises, ELEKS Builds)\n"
            "  • Agentic AI Pilot Development .............. $200K – $500K\n"
            "  • Data Platform Modernization ............... $300K – $1M+\n"
            "  • MLOps / LLMOps Infrastructure ............. $250K – $750K\n\n"
            "TIER 3 — MANAGED SERVICES  (ELEKS-Led)\n"
            "  • AI/ML Model Operations  |  Data Platform Support  |  Agent Monitoring\n\n"
            "Advisory engagements are the top of the funnel — "
            "naturally leading to Tier 2 implementations and ELEKS engineering revenue."
        ),
    },
    {
        "title": "The Brand: A New Name for a New Category",
        "body": (
            "[ CODENAME: ANTIGRAVITY ]\n"
            "\"Helping enterprises defy the gravitational pull of legacy systems — with agentic AI.\"\n\n"
            "BRAND DIRECTION  (final name TBD — in active evaluation)\n"
            "• Abstract / premium naming (e.g., Orion-style: authoritative, navigation metaphor)\n"
            "• Complete separation from ELEKS parent brand\n"
            "• US-first positioning; commands advisory rates from Day 1\n"
            "• Clean domain + trademark clearance required\n\n"
            "TARGET CLIENT\n"
            "• Upper mid-market: $500M – $5B revenue\n"
            "• Fortune 450: $5B – $50B revenue\n"
            "• Buyers: CIO, CTO, CDO, Chief AI Officer, VP Data & Analytics\n\n"
            "TARGET VERTICALS\n"
            "[ Financial Services ]  [ Healthcare & Life Sciences ]  [ Energy ]  [ Government ]\n\n"
            "BRAND PROMISE:  \"Strategy you can implement. Engineering you can trust.\""
        ),
    },
    {
        "title": "Leadership: Proven at Every Level",
        "body": (
            "CEO, ELEKS — Andriy Krupa  (10–20% allocation)\n"
            "Governance, budget approval, board-level strategic direction\n\n"
            "CTO, ELEKS — Alex Shegda  (50–60% allocation  |  Los Angeles, CA)\n"
            "Executive sponsor  |  Direct manager of MD  |  Technical strategy  |  ELEKS delivery coordination\n"
            "25+ years tech strategy  |  MBA IE Business School\n\n"
            "Managing Director & Head of Antigravity — James Sturges  (100% dedicated  |  Boston, MA)\n"
            "P&L ownership  |  US GTM  |  Client relationships  |  Team hiring  |  Brand building\n"
            "20+ years D&A leadership  |  Built practices $0 → $10–15M  |  Big Fed & Fortune 500 consulting\n\n"
            "MD CORE COMPETENCIES\n"
            "1. AI Strategy & Business Alignment (AI Canvas, Capability Maturity Model, ROI quantification)\n"
            "2. Organizational Readiness & AI Transformation Leadership\n"
            "3. Data Infrastructure & AI Platform Strategy (MLOps/LLMOps, cloud-agnostic)\n"
            "4. AI Governance, Risk & Regulatory Compliance (NIST AI RMF, sector-specific)\n"
            "5. C-Suite Engagement & Executive Communication\n"
            "6. Practice Development & Go-to-Market"
        ),
    },
    {
        "title": "Building the Team: Phased for Capital Efficiency",
        "body": (
            "YEAR 1  (~8–10 people)\n"
            "• Managing Director (Boston)\n"
            "• Sr. Solution Architect — Agentic AI (East Coast)\n"
            "• Principal Consultant — Financial Services (NYC/Boston)\n"
            "• Principal Consultant — Healthcare/Life Sciences (Boston/NJ/Chicago)\n"
            "• Business Development Lead  |  Marketing Lead (contractor → FTE)\n"
            "• Senior Consultants ×2  |  Practice Ops Manager (ELEKS internal transfer preferred)\n\n"
            "YEAR 2  (~15–17 people) — adds:\n"
            "• VP Sales (NYC/Chicago/DC)  |  Solution Architect — Data/ML Platforms\n"
            "• Sales Engineer  |  Consultants ×2 (MBA pipeline)  |  Marketing Manager\n\n"
            "YEAR 3  (~25–26 people) — adds:\n"
            "• Principal — Energy (Houston/Denver)  |  Principal — Government (Washington DC)\n"
            "• Senior Consultants ×3  |  Consultants ×2  |  Account Executive\n"
            "• Client Success Lead  |  West Coast presence begins\n\n"
            "LEVERAGE MODEL\n"
            "Small US advisory team + ELEKS' 200+ data engineers & 1,100+ software engineers on demand"
        ),
    },
    {
        "title": "Hiring Strategy: Right Roles, Right Time, Right People",
        "body": (
            "PHASED TIMELINE\n"
            "Phase 0 (Mo 1–3):   MD + Solution Architect + Marketing Contractor\n"
            "Phase 1 (Mo 4–9):   2 Principal Consultants + BD Lead\n"
            "Phase 2 (Mo 10–15): Senior Consultants + 2nd Architect + Ops Manager\n"
            "Phase 3 (Mo 16–24): VP Sales + Sales Engineer + 4 Consultants\n"
            "Phase 4 (Mo 25–36): Energy/Gov Principals + West Coast + Client Success\n\n"
            "FIRST PRIORITY HIRE — Principal Consultant Profile\n"
            "• Big 4 background (Deloitte, EY, KPMG AI/data practice preferred)\n"
            "• Deep data AND agentic AI expertise — cloud agnostic\n"
            "• Strong in Financial Services OR Healthcare/Life Sciences\n"
            "• Can operate independently from Day 1; ability to grow into vertical lead\n\n"
            "SOURCING CHANNELS\n"
            "• Principals & Architects: Executive search (retained) + Big 4 post-bonus attrition (Jan/Jul)\n"
            "• Senior Consultants: LinkedIn Recruiter + employee referral ($10–15K bonus)\n"
            "• Sales/BD: Cloud partner channel referrals (AWS, Snowflake, Databricks)\n"
            "• Junior Consultants: MBA campus (Booth, Kellogg, Fuqua, Darden)\n"
            "• Ops/Admin: ELEKS internal transfer preferred (Chicago/Toronto)\n\n"
            "HIRING GOVERNANCE\n"
            "Roles 1–6: Pre-approved block at program launch\n"
            "Roles 7+:  MD proposes → CTO approves (5-day SLA) → CEO notified"
        ),
    },
    {
        "title": "Compensation & Rewards: Built to Attract Top Talent",
        "body": (
            "STANDARD BENEFITS  (all US FTEs)\n"
            "• Medical/Dental/Vision — employer covers 80%+ of premium\n"
            "• 401(k) with 4% employer match  |  20 days PTO + 12 weeks parental leave\n"
            "• $3,000–$5,000 annual professional development  |  Remote-first with co-working stipend\n\n"
            "COMPENSATION RANGES BY ROLE\n"
            "  Managing Director:      $240K base + 35% bonus + 6% EBITDA profit share\n"
            "  Principal Consultants:  $200–240K base + 25–35% bonus + 1–2% profit share\n"
            "  Solution Architects:    $185–220K base + 20–25% bonus + 1% profit share\n"
            "  Senior Consultants:     $150–180K base + 15–25% bonus\n"
            "  VP Sales:               $180–220K base + OTE $300–350K + 1–2% profit share\n\n"
            "EBITDA PROFIT SHARE MODEL\n"
            "• Total pool capped at 20% of brand EBITDA\n"
            "• 2–3 year cliff vesting, then annual payout\n"
            "• No valuation needed — aligns with bootstrapped, family-owned culture\n"
            "• At $10M revenue / 45% EBITDA margin = $4.5M brand EBITDA:\n"
            "    MD at 6%:          $270K additional annual compensation\n"
            "    Principal at 2%:   $90K additional annual compensation\n"
            "    ELEKS retains:     80%+ of EBITDA"
        ),
    },
    {
        "title": "Managing Director Compensation: James Sturges",
        "body": (
            "BASE SALARY: $240,000\n"
            "Competitive with Tier 2 consulting practice leaders (Slalom, West Monroe, PA Consulting)\n"
            "Boston market + 20+ years experience + greenfield risk premium\n"
            "Review at 18 months → $255–265K upon achieving Year 1 revenue target\n\n"
            "ANNUAL PERFORMANCE BONUS:  Target 35% ($84K)  |  Stretch 50% ($120K)\n"
            "Milestone-based, not discretionary:\n"
            "  Revenue achievement (40%):     Target $2–2.5M Year 1\n"
            "  Client logo acquisition (35%): Target 3–5 logos (min. 1 net-new to ELEKS)\n"
            "  Team build milestones (25%):   6–8 hires; both Principals onboarded\n\n"
            "SIGN-ON BONUS: $40,000  (greenfield risk premium)\n"
            "Paid in 2 tranches: $20K at signing + $20K at 6 months  |  12-month clawback\n\n"
            "EBITDA PROFIT SHARE: 6% of Antigravity brand EBITDA annually\n"
            "Year 1: $0 (brand investing)  |  Year 2: ~$63K  |  Year 3 Target: ~$252K  |  Stretch: ~$423K\n\n"
            "TOTAL COMPENSATION SCENARIOS\n"
            "                    Year 1      Year 2      Year 3    Stretch Y3\n"
            "Base Salary        $240,000    $255,000    $265,000    $275,000\n"
            "Performance Bonus   $84,000     $95,000    $106,000    $165,000\n"
            "EBITDA Profit Sh.        —       $63,000    $252,000    $423,000\n"
            "Sign-On             $40,000          —           —           —\n"
            "TOTAL              $364,000    $413,000    $623,000    $863,000"
        ),
    },
    {
        "title": "Success Milestones & Investment Thesis",
        "body": (
            "THREE-YEAR TARGETS\n"
            "                      Year 1        Year 2        Year 3\n"
            "Revenue              $2 – 3M       $5 – 8M       $10 – 15M\n"
            "Client Logos         3 – 5         10 – 15       20 – 25\n"
            "Team Size            8 – 10        15 – 17       25 – 26\n"
            "EBITDA Margin        10 – 25%      30 – 46%      45 – 57%\n"
            "Pipeline             $5M+          $12M+         $25M+\n\n"
            "KEY GO / NO-GO DECISION POINTS\n"
            "  Month 4–5:   First paid pilot closed → continue Phase 1 hiring\n"
            "  Month 9–10:  $500K cumulative revenue → greenlight Phase 2\n"
            "  Month 12–14: $2M run rate → approve VP Sales hire\n"
            "  Month 16–18: $1M single quarter → greenlight Phase 4 expansion\n"
            "  Month 18–24: Break-even on brand P&L → full Phase 4 investment\n\n"
            "INVESTMENT THESIS\n"
            "  Year 1 investment:      ~$1.7 – 2.3M\n"
            "  Year 3 EBITDA (target):  $4.2 – 6.75M\n"
            "  ROI on initial investment: 2–3× by Year 3\n"
            "  vs. Acquiring a boutique AI firm: $5–15M + integration risk\n\n"
            "At Year 3 target: MD earns 6.2% of $10M revenue. ELEKS captures 93.8%."
        ),
    },
    {
        "title": "Next Steps: From Concept to Launch",
        "body": (
            "IMMEDIATE PRIORITIES  (30 Days)\n"
            "  ☐ Finalize and approve MD compensation package\n"
            "  ☐ Board approval for Year 1 headcount budget (Roles 1–6 pre-approved block)\n"
            "  ☐ Establish Antigravity legal entity structure (LLC vs. ELEKS division)\n"
            "  ☐ Finalize brand name — 12 options evaluated (see naming strategy doc)\n"
            "  ☐ Define ELEKS delivery SLA for Antigravity engagements\n\n"
            "MONTH 1–3  (Foundation)\n"
            "  ☐ MD Day 1: brand setup, partner outreach, pipeline development\n"
            "  ☐ Launch retained search for Senior Solution Architect (East Coast)\n"
            "  ☐ Begin website / brand identity development\n"
            "  ☐ Identify 3–5 ELEKS clients as pilot targets ($50–100K engagements)\n\n"
            "MONTH 4–6  (Market Entry)\n"
            "  ☐ Launch search for Principal Consultant #1 (Financial Services)\n"
            "  ☐ Close first paid pilot engagement\n"
            "  ☐ Publish first thought leadership piece / conference submission\n\n"
            "OPEN QUESTIONS FOR BOARD\n"
            "  1. Legal entity: Separate LLC or ELEKS division?\n"
            "  2. Management fee: What % of Antigravity revenue flows to ELEKS as overhead?\n"
            "  3. ELEKS resource SLA: Guaranteed data engineer availability?\n"
            "  4. Brand name: Final decision timeline?\n\n"
            "\"The window to own agentic AI advisory is open now — but it won't be for long.\""
        ),
    },
]

# Slide dimensions (EMU): 9144000 x 5143500 (standard 16:9)
SLIDE_WIDTH = 9144000
SLIDE_HEIGHT = 5143500

# Layout constants
MARGIN = 457200          # 0.5 inch
TITLE_HEIGHT = 685800    # ~0.75 inch
TITLE_TOP = 274320       # ~0.3 inch
BODY_TOP = TITLE_TOP + TITLE_HEIGHT + 182880  # title + small gap
BODY_HEIGHT = SLIDE_HEIGHT - BODY_TOP - MARGIN


def make_pt(pt):
    return {"magnitude": pt, "unit": "PT"}


def make_color(r, g, b):
    return {"rgbColor": {"red": r / 255, "green": g / 255, "blue": b / 255}}


def add_text_box(slide_id, box_id, text, left, top, width, height,
                 font_size_pt, bold=False, color=(255, 255, 255), bg=None):
    requests = []

    requests.append({
        "createShape": {
            "objectId": box_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": {
                    "width": {"magnitude": width, "unit": "EMU"},
                    "height": {"magnitude": height, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": left, "translateY": top,
                    "unit": "EMU",
                },
            },
        }
    })

    requests.append({
        "insertText": {
            "objectId": box_id,
            "text": text,
            "insertionIndex": 0,
        }
    })

    style = {
        "bold": bold,
        "fontSize": make_pt(font_size_pt),
        "foregroundColor": {"opaqueColor": make_color(*color)},
        "fontFamily": "Arial",
    }
    requests.append({
        "updateTextStyle": {
            "objectId": box_id,
            "style": style,
            "textRange": {"type": "ALL"},
            "fields": "bold,fontSize,foregroundColor,fontFamily",
        }
    })

    if bg:
        requests.append({
            "updateShapeProperties": {
                "objectId": box_id,
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {"color": {"rgbColor": {
                            "red": bg[0] / 255,
                            "green": bg[1] / 255,
                            "blue": bg[2] / 255,
                        }}}
                    }
                },
                "fields": "shapeBackgroundFill",
            }
        })

    return requests


def set_slide_background(slide_id, r, g, b):
    return [{
        "updatePageProperties": {
            "objectId": slide_id,
            "pageProperties": {
                "pageBackgroundFill": {
                    "solidFill": {
                        "color": {"rgbColor": {
                            "red": r / 255,
                            "green": g / 255,
                            "blue": b / 255,
                        }}
                    }
                }
            },
            "fields": "pageBackgroundFill",
        }
    }]


def build_slide_requests(slide_id, slide_index, title, body):
    requests = []
    is_cover = slide_index == 0

    # Background: deep navy for cover, dark slate for content slides
    if is_cover:
        requests += set_slide_background(slide_id, 10, 22, 60)   # deep navy
    else:
        requests += set_slide_background(slide_id, 18, 30, 70)   # dark slate blue

    box_prefix = slide_id.replace("-", "_")

    if is_cover:
        # Cover: large centred title + subtitle
        requests += add_text_box(
            slide_id, f"{box_prefix}_title",
            title,
            left=MARGIN, top=SLIDE_HEIGHT // 4,
            width=SLIDE_WIDTH - 2 * MARGIN, height=900000,
            font_size_pt=44, bold=True,
            color=(255, 255, 255),
        )
        requests += add_text_box(
            slide_id, f"{box_prefix}_body",
            body,
            left=MARGIN, top=SLIDE_HEIGHT // 4 + 950000,
            width=SLIDE_WIDTH - 2 * MARGIN, height=700000,
            font_size_pt=18, bold=False,
            color=(180, 200, 255),
        )
        # Accent line (thin coloured bar)
        requests.append({
            "createShape": {
                "objectId": f"{box_prefix}_accent",
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {
                        "width": {"magnitude": SLIDE_WIDTH - 2 * MARGIN, "unit": "EMU"},
                        "height": {"magnitude": 60000, "unit": "EMU"},
                    },
                    "transform": {
                        "scaleX": 1, "scaleY": 1,
                        "translateX": MARGIN,
                        "translateY": SLIDE_HEIGHT // 4 - 80000,
                        "unit": "EMU",
                    },
                },
            }
        })
        requests.append({
            "updateShapeProperties": {
                "objectId": f"{box_prefix}_accent",
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {"color": {"rgbColor": {
                            "red": 0.18, "green": 0.53, "blue": 1.0
                        }}}
                    },
                    "outline": {"propertyState": "NOT_RENDERED"},
                },
                "fields": "shapeBackgroundFill,outline",
            }
        })
    else:
        # Content slides: title bar + body text
        # Title background bar
        requests.append({
            "createShape": {
                "objectId": f"{box_prefix}_titlebg",
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {
                        "width": {"magnitude": SLIDE_WIDTH, "unit": "EMU"},
                        "height": {"magnitude": TITLE_HEIGHT + TITLE_TOP + 91440, "unit": "EMU"},
                    },
                    "transform": {
                        "scaleX": 1, "scaleY": 1,
                        "translateX": 0, "translateY": 0,
                        "unit": "EMU",
                    },
                },
            }
        })
        requests.append({
            "updateShapeProperties": {
                "objectId": f"{box_prefix}_titlebg",
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {"color": {"rgbColor": {
                            "red": 10 / 255, "green": 22 / 255, "blue": 60 / 255,
                        }}}
                    },
                    "outline": {"propertyState": "NOT_RENDERED"},
                },
                "fields": "shapeBackgroundFill,outline",
            }
        })

        # Title text
        requests += add_text_box(
            slide_id, f"{box_prefix}_title",
            title,
            left=MARGIN, top=TITLE_TOP,
            width=SLIDE_WIDTH - 2 * MARGIN, height=TITLE_HEIGHT,
            font_size_pt=24, bold=True,
            color=(255, 255, 255),
        )

        # Slide number (top right)
        requests += add_text_box(
            slide_id, f"{box_prefix}_num",
            str(slide_index + 1),
            left=SLIDE_WIDTH - MARGIN - 300000, top=TITLE_TOP,
            width=300000, height=TITLE_HEIGHT,
            font_size_pt=14, bold=False,
            color=(100, 140, 220),
        )

        # Body text
        requests += add_text_box(
            slide_id, f"{box_prefix}_body",
            body,
            left=MARGIN, top=BODY_TOP,
            width=SLIDE_WIDTH - 2 * MARGIN, height=BODY_HEIGHT,
            font_size_pt=13, bold=False,
            color=(220, 230, 255),
        )

        # Blue accent line under title bar
        requests.append({
            "createShape": {
                "objectId": f"{box_prefix}_accent",
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {
                        "width": {"magnitude": SLIDE_WIDTH, "unit": "EMU"},
                        "height": {"magnitude": 45720, "unit": "EMU"},
                    },
                    "transform": {
                        "scaleX": 1, "scaleY": 1,
                        "translateX": 0,
                        "translateY": TITLE_TOP + TITLE_HEIGHT + 91440,
                        "unit": "EMU",
                    },
                },
            }
        })
        requests.append({
            "updateShapeProperties": {
                "objectId": f"{box_prefix}_accent",
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {"color": {"rgbColor": {
                            "red": 0.18, "green": 0.53, "blue": 1.0
                        }}}
                    },
                    "outline": {"propertyState": "NOT_RENDERED"},
                },
                "fields": "shapeBackgroundFill,outline",
            }
        })

    return requests


def main():
    creds = pickle.load(open(TOKEN_PATH, "rb"))
    service = build("slides", "v1", credentials=creds)

    pres = service.presentations().get(presentationId=PRESENTATION_ID).execute()
    slides = pres["slides"]

    print(f"Found {len(slides)} slides. Building content requests...")

    all_requests = []
    for i, (slide, content) in enumerate(zip(slides, SLIDE_CONTENT)):
        slide_id = slide["objectId"]
        print(f"  Slide {i+1}: {slide_id} — {content['title'][:50]}")
        all_requests += build_slide_requests(
            slide_id, i, content["title"], content["body"]
        )

    print(f"\nSending {len(all_requests)} API requests in one batch...")
    result = service.presentations().batchUpdate(
        presentationId=PRESENTATION_ID,
        body={"requests": all_requests},
    ).execute()

    print(f"Done. Replies: {len(result.get('replies', []))}")
    print(f"\nOpen deck: https://docs.google.com/presentation/d/{PRESENTATION_ID}")


if __name__ == "__main__":
    main()
