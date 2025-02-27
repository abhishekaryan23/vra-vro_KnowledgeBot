from ragas import evaluate, EvaluationDataset
from ragas.llms import LangchainLLMWrapper

def evaluate_rag(dataset):
    evaluation_dataset = EvaluationDataset.from_list(dataset)
    evaluator_llm = LangchainLLMWrapper(llm)
    metrics = [LLMContextRecall(), Faithfulness(), FactualCorrectness()]
    result = evaluate(dataset=evaluation_dataset, metrics=metrics, llm=evaluator_llm)
    return result