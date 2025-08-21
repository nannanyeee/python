sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 180, "인천"),
    (2020, 3, "스마트폰", 650, 160, "서울"),
    (2020, 4, "노트북", 1400, 130, "부산"),
    (2020, 4, "스마트폰", 900, 190, "서울"),
    (2021, 1, "노트북", 1300, 170, "대구"),
    (2021, 1, "스마트폰", 950, 140, "인천"),
    (2021, 2, "노트북", 1100, 160, "서울"),
    (2021, 2, "스마트폰", 800, 180, "부산"),
    (2021, 3, "노트북", 1300, 150, "대구"),
    (2021, 3, "스마트폰", 800, 200, "서울"),
    (2021, 4, "노트북", 1300, 170, "부산"),
    (2021, 4, "스마트폰", 800, 190, "서울")
]

#연도별 판매량 계산
yearly_sales = {}
for year, quarter, product, price, sales, region in sales_data:
    if year not in yearly_sales:
        yearly_sales[year] = {}
    if product not in yearly_sales[year]:
        yearly_sales[year][product] = 0
    yearly_sales[year][product] += sales
    
print("연도별 판매량:")
for year, products in yearly_sales.items():
    print(f"{year}: {products}")

#제품별 평균 가격 계산
average_price = {}
for year, quarter, product, price, sales, region in sales_data:
    if product not in average_price:
        average_price[product] = []
    average_price[product].append(price)

print("\n제품별 평균 가격:")
for product, prices in average_price.items():
    print(f"{product}: {sum(prices)/len(prices):.2f}")

#최대 판매 지역 찾기
max_sales_region = {}
for year, quarter, product, price, sales, region in sales_data:
    if region not in max_sales_region:
        max_sales_region[region] = 0
    max_sales_region[region] += sales

max_region = max(max_sales_region, key=max_sales_region.get)
print(f"\n최대 판매 지역: {max_region} ({max_sales_region[max_region]}개 판매)")

#분기별 매출 분석
quarterly_sales = {}
for year, quarter, product, price, sales, region in sales_data:
    if (year, quarter) not in quarterly_sales:
        quarterly_sales[(year, quarter)] = 0
    quarterly_sales[(year, quarter)] += price * sales

print("\n분기별 매출:")
for (year, quarter), total_sales in quarterly_sales.items():
    print(f"{year}년 {quarter}분기: {total_sales}원")