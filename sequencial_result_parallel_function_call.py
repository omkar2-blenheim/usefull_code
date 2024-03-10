import asyncio

async def async_function(item):
    # Your asynchronous function that takes some time to process
    await asyncio.sleep(2)  # Simulating some asynchronous work
    return f"Processed: {item}"

async def process_item(semaphore, item):
    print("fumction ", str(item))
    async with semaphore:
        print("inside semaphore", str(item))
        result = await async_function(item)
        return result

async def main():
    items = [1, 2, 3, 4, 5,6,8,9,0]

    # Create a list to store the results
    results = []

    # Set the semaphore limit to 3 concurrent calls
    semaphore = asyncio.Semaphore(3)

    # Use asyncio.gather to asynchronously call the function for each item
    tasks = [process_item(semaphore, item) for item in items]
    responses = await asyncio.gather(*tasks)

    # Process the responses sequentially
    for response in responses:
        # Do something with the response
        results.append(response)

    # Print the results
    print(results)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
