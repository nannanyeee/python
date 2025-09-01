# 5개의 공개 API URL에 GET요청을 보냄
# 순차처리
# ThreadPoolExecutor - (멀티스레드 병렬 처리)여러 개의 스레드를 동시에 실행하여 요청을 병렬 처리 / 스레드 여러 개가 각자 하나의 작업 실행
# asyncio와 aiohttp - (비동기 처리) async, await 기반 비동기 프로그래밍 활용 / 이벤트 루프기반으로 한 스레드가 여러 작업을 번갈아 실행 / I/O대기 시간에 다른 작업으로 전환됨

import time
from concurrent.futures import ThreadPoolExecutor, as_completed #I/O 바운드 작업을 스레드로 동시에 실행
import asyncio #이벤트 루프/코루틴/태스크 스케줄링
import aiohttp #비동기 HTTP 클라이언트
import requests #동기 HTTP 클라이언트

websites = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5"
]

# 비동기적으로 웹사이트 내용 가져오기 
async def fetch(session, url):
    print(f"{url} 요청 시작")
    try:
        start_time = time.time()
        async with session.get(url, timeout=10) as response:
            content = await response.text()
            elapsed = time.time() - start_time
            print(f"{url} 응답 완료: {len(content)} 바이트 (소요시간: {elapsed:.2f}초)")
            return url, len(content), elapsed
    except Exception as e:
        print(f"{url} 오류 발생: {e}")
        return url, 0, 0
    
#순차처리
def fetch_all_sequential(urls):
    start_time = time.time()
    results = []

    for url in urls:
        resp = requests.get(url, timeout=10)
        size = len(resp.text)
        print(f"{url} 응답 완료: {size} 바이트")
        results.append((url, len(resp.text)))
    elapsed = time.time() - start_time
    print(f"\n[순차 처리 완료] {elapsed:.2f}초 소요")
    return results

#ThreadPoolExecutor
def fetch_request(url):
    resp = requests.get(url, timeout=10)
    return url, len(resp.text)

def fetch_threadpool(urls):
    start = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_request, url) for url in urls]
        for f in as_completed(futures):
            url, size = f.result()
            print(f"{url} 응답 완료: {size} 바이트")
            results.append((url,size))
    elapsed = time.time() - start
    print(f"\n[ThreadPoolExecutor 처리 완료] {elapsed:.2f}초 소요\n")
    return results

#asyncio와 aiohttp
async def fetch_async(session, url):
    async with session.get(url, timeout = 10) as resp:
        text = await resp.text()
        return url, len(text)

async def fetch_asyncio(urls):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, size in results:
            print(f"{url} 응답 완료: {size} 바이트")
    elapsed = time.time() - start
    print(f"\n[asyncio + aiohttp 처리 완료] {elapsed:.2f}초 소요\n")
    return results

async def main():
    print("\n=== 순차 처리 시작 ===")
    sequential_results = fetch_all_sequential(websites)

    await asyncio.sleep(1)

    print("\n=== ThreadPoolExecutor 시작 ===")
    th_results = fetch_threadpool(websites)

    await asyncio.sleep(1)

    print("\n=== asyncio와 aiohttp 시작 ===")
    async_results= await fetch_asyncio(websites)

    print("\n=== 결과 요약 ===")
    seq_total_bytes = sum(r[1] for r in sequential_results)
    th_total_bytes = sum(r[1] for r in th_results)
    async_total_bytes = sum(r[1] for r in async_results)

    print(f"순차 처리: 총 {seq_total_bytes} 바이트")
    print(f"ThreadPoolExecutor 처리: 총 {th_total_bytes} 바이트")
    print(f"asyncio + aiohttp 처리: 총 {async_total_bytes} 바이트")

if __name__ == "__main__":
    asyncio.run(main())