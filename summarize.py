import cohere

# Setting up the client
api_key = "XjReiHQdMxMRNVMDybIcUpfMgFyevfkdYYmjVg1j"
co = cohere.Client(api_key)


def summarize(prompt: str) -> str:
    result = co.summarize(
        text=prompt,
        length='medium',
        format='bullets'
    )

    temp = result.summary.split("- ")
    formatted = ""
    for i in range(1, len(temp)):
        formatted += ("- " + temp[i] + "\n")
    return formatted


