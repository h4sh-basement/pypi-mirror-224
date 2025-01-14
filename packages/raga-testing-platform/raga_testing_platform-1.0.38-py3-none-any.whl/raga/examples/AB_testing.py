from raga import *

#create test_session object of TestSession instance
test_session = TestSession(project_name="testingProject", #Project Name
                           run_name="test-8-aug-v2", #Experiment Name
                           u_test=True)

test_session.token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbkByYWdhIiwicm9sZXMiOlsiUk9MRV9BRE1JTiJdLCJ1c2VyTmFtZSI6ImFkbWluQHJhZ2EiLCJleHAiOjE2OTE1NTgwNTYsImlhdCI6MTY5MTQ3MTY1Niwib3JnSWQiOjEsImp0aSI6ImFkbWluQHJhZ2EifQ.jhDiidIdA2AFuNgWuFAwM2iTdXZHb7wvlaaM-nptakni6QvGh0QscFj-3tKTvEna1hqjNyx0mo9lhpnFtxgqOg"
test_session.project_id = 1
test_session.experiment_id = 1701
#create payload for model ab testing
rules = ModelABTestRules() 
rules.add(metric="precision_diff_all", IoU=0.5, _class="All", threshold=0.5)

model_comparison_check = model_ab_test(test_session=test_session, 
                                       dataset_name="dataset-7-aug-v3",
                                       test_name="AB-test-8-aug-v3",
                                       modelA = "modelA", 
                                       modelB = "modelB" ,
                                       type = "labelled", 
                                       gt="GT",
                                       rules = rules,
                                       aggregation_level=["location", "vehicle_no", "date_captured", "channel", "dataset_type"])

# add payload into test_session object
test_session.add(model_comparison_check)

# #run added ab test model payload
test_session.run()