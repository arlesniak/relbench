from torch_frame import stype

# TODO (joshrob) move to dataset definition datasets/amazon.py etc.

dataset2inferred_stypes = {
    "rel-hm": {
        "article": {
            "article_id": stype.numerical,
            "product_code": stype.numerical,
            "prod_name": stype.text_embedded,
            "product_type_no": stype.numerical,
            "product_type_name": stype.categorical,
            "product_group_name": stype.categorical,
            "graphical_appearance_no": stype.categorical,
            "graphical_appearance_name": stype.categorical,
            "colour_group_code": stype.categorical,
            "colour_group_name": stype.categorical,
            "perceived_colour_value_id": stype.categorical,
            "perceived_colour_value_name": stype.categorical,
            "perceived_colour_master_id": stype.numerical,
            "perceived_colour_master_name": stype.categorical,
            "department_no": stype.numerical,
            "department_name": stype.categorical,
            "index_code": stype.categorical,
            "index_name": stype.categorical,
            "index_group_no": stype.categorical,
            "index_group_name": stype.categorical,
            "section_no": stype.numerical,
            "section_name": stype.text_embedded,
            "garment_group_no": stype.categorical,
            "garment_group_name": stype.categorical,
            "detail_desc": stype.text_embedded,
        },
        "customer": {
            "customer_id": stype.text_embedded,
            "FN": stype.categorical,
            "Active": stype.categorical,
            "club_member_status": stype.categorical,
            "fashion_news_frequency": stype.categorical,
            "age": stype.numerical,
            "postal_code": stype.categorical,
        },
        "transactions": {
            "t_dat": stype.timestamp,
            "price": stype.numerical,
            "sales_channel_id": stype.categorical,
        },
    },
    "rel-amazon": {
        "product": {
            "product_id": stype.numerical,
            "brand": stype.text_embedded,
            "title": stype.text_embedded,
            "description": stype.text_embedded,
            "price": stype.numerical,
            "category": stype.multicategorical,
        },
        "customer": {
            "customer_id": stype.numerical,
            "customer_name": stype.text_embedded,
        },
        "review": {
            "review_text": stype.text_embedded,
            "summary": stype.text_embedded,
            "review_time": stype.timestamp,
            "rating": stype.numerical,
            "verified": stype.categorical,
            "customer_id": stype.numerical,
            "product_id": stype.numerical,
        },
    },
    "rel-stackex": {
        "postLinks": {
            "Id": stype.numerical,
            "RelatedPostId": stype.numerical,
            "PostId": stype.numerical,
            "LinkTypeId": stype.numerical,
            "CreationDate": stype.timestamp,
        },
        "posts": {
            "Id": stype.numerical,
            "PostTypeId": stype.numerical,
            "AcceptedAnswerId": stype.numerical,
            "ParentId": stype.numerical,
            "CreationDate": stype.timestamp,
            "Body": stype.text_embedded,
            "OwnerUserId": stype.numerical,
            # "LastEditorUserId": stype.numerical,
            # Uninformative text column
            # "LastEditorDisplayName": stype.text_embedded,
            "Title": stype.text_embedded,
            "Tags": stype.text_embedded,
        },
        "users": {
            "Id": stype.numerical,
            "AccountId": stype.numerical,
            "CreationDate": stype.timestamp,
            # Uninformative text column
            # "DisplayName": stype.text_embedded,
            # "Location": stype.text_embedded,
            "AboutMe": stype.text_embedded,
            # Uninformative text column
            # "WebsiteUrl": stype.text_embedded,
        },
        "votes": {
            "Id": stype.numerical,
            "PostId": stype.numerical,
            "VoteTypeId": stype.numerical,
            "UserId": stype.numerical,
            "CreationDate": stype.timestamp,
        },
        "comments": {
            "Id": stype.numerical,
            "PostId": stype.numerical,
            "Text": stype.text_embedded,
            "CreationDate": stype.timestamp,
            "UserId": stype.numerical,
            # Uninformative text column
            # "UserDisplayName": stype.text_embedded,
            # "ContentLicense": stype.text_embedded,
        },
        "badges": {
            "Id": stype.numerical,
            "UserId": stype.numerical,
            "Class": stype.categorical,
            # Uninformative text column
            # "Name": stype.text_embedded,
            "Date": stype.timestamp,
            "TagBased": stype.categorical,
        },
        "postHistory": {
            "Id": stype.numerical,
            "PostId": stype.numerical,
            "UserId": stype.numerical,
            "PostHistoryTypeId": stype.numerical,
            # Uninformative text column
            # "UserDisplayName": stype.text_embedded,
            "ContentLicense": stype.categorical,
            # Uninformative text column
            # "RevisionGUID": stype.text_embedded,
            "Text": stype.text_embedded,
            # Uninformative text column
            # "Comment": stype.text_embedded,
            "CreationDate": stype.timestamp,
        },
    },
    "rel-f1": {
        "races": {
            "raceId": stype.numerical,
            "year": stype.numerical,
            "round": stype.numerical,
            "circuitId": stype.numerical,
            "name": stype.text_embedded,
            "date": stype.timestamp,
            "time": stype.timestamp,
        },
        "circuits": {
            "circuitId": stype.numerical,
            "circuitRef": stype.text_embedded,
            "name": stype.text_embedded,
            "location": stype.text_embedded,
            "country": stype.categorical,
            "lat": stype.numerical,
            "lng": stype.numerical,
            # "alt": stype.numerical,
        },
        "drivers": {
            "driverId": stype.numerical,
            "driverRef": stype.text_embedded,
            "code": stype.text_embedded,
            "forename": stype.text_embedded,
            "surname": stype.text_embedded,
            "dob": stype.timestamp,
            "nationality": stype.categorical,
        },
        "results": {
            "resultId": stype.numerical,
            "raceId": stype.numerical,
            "driverId": stype.numerical,
            "constructorId": stype.numerical,
            "statusId": stype.categorical,
            "number": stype.numerical,
            "grid": stype.numerical,
            "position": stype.numerical,
            "positionOrder": stype.numerical,
            "points": stype.numerical,
            "laps": stype.numerical,
            # "time": stype.timestamp,
            "milliseconds": stype.numerical,
            "fastestLap": stype.numerical,
            "rank": stype.numerical,
            # "fastestLapTime": stype.timestamp,
            # "fastestLapSpeed": stype.numerical,
            "date": stype.timestamp,
        },
        "standings": {
            "driverStandingsId": stype.numerical,
            "raceId": stype.numerical,
            "driverId": stype.numerical,
            "points": stype.numerical,
            "position": stype.numerical,
            "wins": stype.numerical,
            "date": stype.timestamp,
        },
        "constructors": {
            "constructorId": stype.numerical,
            "constructorRef": stype.text_embedded,
            "name": stype.text_embedded,
            "nationality": stype.categorical,
        },
        "constructor_results": {
            "constructorResultsId": stype.numerical,
            "raceId": stype.numerical,
            "constructorId": stype.numerical,
            "points": stype.numerical,
            "status": stype.text_embedded,
            "date": stype.timestamp,
        },
        "constructor_standings": {
            "constructorStandingsId": stype.numerical,
            "raceId": stype.numerical,
            "constructorId": stype.numerical,
            "points": stype.numerical,
            "position": stype.numerical,
            "wins": stype.numerical,
            "date": stype.timestamp,
        },
        "qualifying": {
            "qualifyId": stype.numerical,
            "raceId": stype.numerical,
            "driverId": stype.numerical,
            "constructorId": stype.numerical,
            "number": stype.numerical,
            "position": stype.numerical,
            # "q1": stype.timestamp,
            # "q2": stype.timestamp,
            # "q3": stype.timestamp,
        },
        "lap_times": {
            "lapId": stype.numerical,
            "raceId": stype.numerical,
            "driverId": stype.numerical,
            "lap": stype.numerical,
            "position": stype.numerical,
            # "time": stype.timestamp,
            "milliseconds": stype.numerical,
        },
    },
    "rel-trial": {
        "studies": {
            "nct_id": stype.numerical,
            "start_date": stype.timestamp,
            "target_duration": stype.text_embedded,
            "study_type": stype.categorical,
            "acronym": stype.text_embedded,
            "baseline_population": stype.text_embedded,
            "brief_title": stype.text_embedded,
            "official_title": stype.text_embedded,
            "phase": stype.categorical,
            "enrollment": stype.numerical,
            "enrollment_type": stype.categorical,
            "source": stype.text_embedded,
            "number_of_arms": stype.numerical,
            "number_of_groups": stype.numerical,
            "has_dmc": stype.categorical,
            "is_fda_regulated_drug": stype.categorical,
            "is_fda_regulated_device": stype.categorical,
            "is_unapproved_device": stype.categorical,
            "is_ppsd": stype.text_embedded,
            "is_us_export": stype.categorical,
            "biospec_retention": stype.categorical,
            "biospec_description": stype.text_embedded,
            "source_class": stype.categorical,
            "baseline_type_units_analyzed": stype.text_embedded,
            "fdaaa801_violation": stype.categorical,
            "plan_to_share_ipd": stype.categorical,
            "detailed_descriptions": stype.text_embedded,
            "brief_summaries": stype.text_embedded,
        },
        "outcomes": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "outcome_type": stype.categorical,
            "title": stype.text_embedded,
            "description": stype.text_embedded,
            "time_frame": stype.text_embedded,
            "population": stype.text_embedded,
            "units": stype.text_embedded,
            "units_analyzed": stype.text_embedded,
            "dispersion_type": stype.text_embedded,
            "param_type": stype.categorical,
            "date": stype.timestamp,
        },
        "outcome_analyses": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "outcome_id": stype.numerical,
            "non_inferiority_type": stype.categorical,
            "non_inferiority_description": stype.text_embedded,
            "param_type": stype.text_embedded,
            "param_value": stype.numerical,
            "dispersion_type": stype.categorical,
            "dispersion_value": stype.numerical,
            "p_value_modifier": stype.text_embedded,
            "p_value": stype.numerical,
            "ci_n_sides": stype.categorical,
            "ci_percent": stype.numerical,
            "ci_lower_limit": stype.numerical,
            "ci_upper_limit": stype.numerical,
            "ci_upper_limit_na_comment": stype.text_embedded,
            "p_value_description": stype.text_embedded,
            "method": stype.text_embedded,
            "method_description": stype.text_embedded,
            "estimate_description": stype.text_embedded,
            "groups_description": stype.text_embedded,
            "other_analysis_description": stype.text_embedded,
            "date": stype.timestamp,
        },
        "drop_withdrawals": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "period": stype.text_embedded,
            "reason": stype.text_embedded,
            "count": stype.numerical,
            "date": stype.timestamp,
        },
        "reported_event_totals": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "event_type": stype.categorical,
            "classification": stype.categorical,
            "subjects_affected": stype.numerical,
            "subjects_at_risk": stype.numerical,
            "date": stype.timestamp,
        },
        "designs": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "allocation": stype.categorical,
            "intervention_model": stype.categorical,
            "observational_model": stype.categorical,
            "primary_purpose": stype.text_embedded,
            "time_perspective": stype.categorical,
            "masking": stype.categorical,
            "masking_description": stype.text_embedded,
            "intervention_model_description": stype.text_embedded,
            "subject_masked": stype.categorical,
            "caregiver_masked": stype.categorical,
            "investigator_masked": stype.categorical,
            "outcomes_assessor_masked": stype.categorical,
            "date": stype.timestamp,
        },
        "eligibilities": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "sampling_method": stype.categorical,
            "gender": stype.categorical,
            "minimum_age": stype.text_embedded,
            "maximum_age": stype.text_embedded,
            "healthy_volunteers": stype.categorical,
            "population": stype.text_embedded,
            "criteria": stype.text_embedded,
            "gender_description": stype.text_embedded,
            "gender_based": stype.categorical,
            "adult": stype.categorical,
            "child": stype.categorical,
            "older_adult": stype.categorical,
            "date": stype.timestamp,
        },
        "interventions": {
            "intervention_id": stype.numerical,
            "mesh_term": stype.text_embedded,
        },
        "conditions": {
            "condition_id": stype.numerical,
            "mesh_term": stype.text_embedded,
        },
        "facilities": {
            "facility_id": stype.numerical,
            "name": stype.text_embedded,
            "city": stype.text_embedded,
            "state": stype.text_embedded,
            "zip": stype.text_embedded,
            "country": stype.text_embedded,
        },
        "sponsors": {
            "sponsor_id": stype.numerical,
            "name": stype.text_embedded,
            "agency_class": stype.categorical,
        },
        "interventions_studies": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "intervention_id": stype.numerical,
            "date": stype.timestamp,
        },
        "conditions_studies": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "condition_id": stype.numerical,
            "date": stype.timestamp,
        },
        "facilities_studies": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "facility_id": stype.numerical,
            "date": stype.timestamp,
        },
        "sponsors_studies": {
            "id": stype.numerical,
            "nct_id": stype.numerical,
            "sponsor_id": stype.numerical,
            "lead_or_collaborator": stype.categorical,
            "date": stype.timestamp,
        },
    },
}
