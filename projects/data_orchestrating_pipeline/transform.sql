with raw_data as (
    select * from {{ ref('feature_data_raw') }}
)

select *,
       case when feature_1 = 1 then 12 else feature_1 end as feature_1,
       case when feature_2 = 1 then 12 else feature_2 end as feature_2,
       case when feature_3 = 1 then 12 else feature_3 end as feature_3,
       case when feature_4 = 1 then 12 else feature_4 end as feature_4,
       case when feature_5 = 1 then 12 else feature_5 end as feature_5,
       case when feature_6 = 1 then 12 else feature_6 end as feature_6,
       case when feature_7 = 1 then 12 else feature_7 end as feature_7,
       case when feature_8 = 1 then 12 else feature_8 end as feature_8,
       case when feature_9 = 1 then 12 else feature_9 end as feature_9,
       case when feature_10 = 1 then 12 else feature_10 end as feature_10,
       (feature_1 + feature_2 + feature_3 + feature_4 + feature_5 + feature_6 + feature_7 + feature_8 + feature_9 + feature_10) as target
from raw_data
