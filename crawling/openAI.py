import requests
from dotenv import load_dotenv
from trandlator.jobs_status import is_job_registered,job_id
import os
import json

def trans_summ_data(crawled_data: str):
    if is_job_registered(job_id) == False:
        return (False,None)
    
    # Configuration
    load_dotenv()
    API_KEY = os.environ.get('API_KEY')
    #IMAGE_PATH = "YOUR_IMAGE_PATH"
    #encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }
    prompt = """영어 뉴스 기사의 주 내용을 파악하고 한국어로 번역하세요. 크롤링된 데이터에는 관련 없는 내용이 포함될 수 있으므로, 그런 내용은 무시하고 배제하십시오. 핵심 내용을 기준으로 한국어 제목, 번역본, 요약본을 작성하세요. 그런 다음, 결과를 JSON 형태로 출력하세요.​
​
# Steps​
1. **기사 분석** ​
   - 기사의 주요 내용을 파악하여 관련 없는 부분은 제외합니다.​
2. **번역 작업**​
   - 주 내용을 기반으로 영어 기사를 한국어로 번역합니다.​
3. **요약 작성**​
   - 주요 내용을 간결하게 요약합니다.​
4. **타이틀 작성**​
   - 번역한 내용에 어울리는 적절한 한국어 제목을 작성합니다.​
​
# Output Format​
- JSON 형식으로 출력합니다.​
- 구조: `{"k_title": "한국어 제목", "k_article": "한국어 번역", "k_summary": "한국어 요약"}`​
- 데이터가 부족하거나 이상하면 `k_title`의 값에 `"error"`를 입력합니다.​
​
# Examples​
**Input:** ​
- A news article in English with some extraneous content.​
​
**Output:**​
```json
{​
  "k_title": "뉴스의 주요 흐름에 맞는 한국어 제목",​
  "k_article": "영어 기사의 주요 내용을 번역한 한국어 텍스트. 기사 전체가 정돈되고 일관된 구조를 가지고, 문맥과 중요한 내용에 맞추어 번역.",​
  "k_summary": "주요 요점을 간략히 정리한 한국어 요약."​
}​
```​
​
# Notes​
​
- 번역이 어려운 구문은 문맥에 맞게 한국어로 자연스럽게 표현하세요.​
- 크롤링 데이터의 질이 불확실할 수 있으므로 기사 분석 단계에서 비중 있는 내용을 선별해내는 것이 중요합니다.​​"""
    # Payload for the request
    payload = {
    "messages": [
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": prompt
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": crawled_data
            }
        ]
        }
    ],
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 1500
    }

    ENDPOINT = os.environ.get('ENDPOINT')

    # Send request
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        #response.encoding = 'utf-8'
        response_json = response.json()
        message = response_json['choices'][0]['message']['content']
        
        message = message.strip('```json').strip('```').strip()
        json_data = json.loads(message)
        #print(message)
        return (True,json_data)
    except requests.RequestException as e:
        print(f"Open AI Request failed. Error: {e}")
        return (False,None)

#if __name__ == "__main__":
    #data = 
    """(Bloomberg) -- Jade Barnett was 15 when she was driven 250 miles away from her home in London to Blackpool, in the northwest of England. There, she was sent to live in a privately owned children’s home.

Most Read from Bloomberg

Hong Kong's Expat Party Hub Reshaped by Chinese Influx

How California Sees the World, and Itself

City Hall Is Hiring

American Institute of Architects CEO Resigns

London’s Tube Fares Are Set to Rise by 4.6% Next Year


“Being moved to a rural area was a hard transition,” says Barnett, now 24, who’d lived in London for most of her life. As a Black teenager, she struggled with the change. “I never saw anyone who looked like me.”

Her story is becoming a common one in Britain, and it goes to the heart of an increasingly tense stand-off between the private companies who’ve come to dominate this sector and the regulators and politicians who police them. With four out of five UK children’s homes now in private hands — many run by companies backed by investment giants such as Ares Management Corp. and Abu Dhabi’s sovereign wealth fund — lawmakers are starting to ask: At what cost?

Barnett’s experience is a case in point. Charities say tales like hers are evidence that private firms are housing vulnerable kids in cheaper parts of the country rather than where they’re from. For-profit operators counter that such claims are unfair, and that children’s welfare is their priority. But the way they do business is coming under intense scrutiny.


As critics debate the inroads that private capital has made into many corners of the economy and public services — in Britain and elsewhere — children’s services are a flashpoint. Bridget Phillipson, education secretary for the new Labour government, has called out private providers for making “excessive profits,” and she’s readying a crackdown.

Across England, there are 3,491 children’s homes, with more than 14,000 beds. Even though there are still hundreds of smaller for-profit operators, a select group of companies backed by private capital has begun to hold sway. Rewards can be lucrative, according to the Local Government Association, with average profit margins for the big providers of more than 20%. Their lenders can charge interest rates close to 10%, Bloomberg analysis estimates.

“We’re aware that some registered children’s homes have become an investment vehicle for private equity, often based overseas,” says Yvette Stanley, national director of social care at Ofsted, the regulator for this market. “Many private firms do a good job. But we’re worried about the risks of so many services supporting vulnerable children being held in so few private hands. And we don’t have the right tools to regulate them.”

Some of the financing is complex, too, adding to the difficulties of keeping tabs. Buyout firm G Square Capital, for example, owns the second-largest children’s homes provider, Keys Group Ltd., and in 2022 sold it on to a €500 million ($525 million) “continuation fund,” a practice where PE firms typically sell companies to a new fund that they also run, in order to raise cash.

For their part, private companies say that without their spending, the UK wouldn’t cope with the rampant demand for places, and specialist care. G Square didn’t respond to requests for comment on its financing.


“Too often, when phrases such as ‘profiteering’ are used, it diminishes not only the dedicated work of professionals within the private sector, but also the levels of private investment that has been needed to meet the increasing needs of children and young people,” says Andrew Isaac, independent chair of the Children’s Services Development Group, a body representing providers.

The sector cares for “some of the most vulnerable children,” he adds, filling “significant gaps” that “the state has failed to provide over many years.”

Duty of Care

Privatization in the UK sped up as the number of children taken into care rose rapidly during the 2000s, following the tragic killings of eight-year old Victoria Climbié and toddler Peter Connelly by family members.

About 50,000 kids were cared for by the state in England in the late 1990s, rising to 83,630 as of March 31, government statistics show. Most are fostered but overall local government spending on looked-after children more than doubled in a decade, from £3.1 billion in 2009/10 to £7 billion in 2022/23.


As the need for places became ever more acute, and as post-financial crisis austerity meant councils couldn’t afford the upfront costs of meeting that need, private provision was regularly seen as the only answer. Some of the marquee names of global capital have happily stepped in.

Before this shift the UK children’s homes sector was mainly fragmented, with private local companies working alongside publicly owned residences. In recent years, lots of these smaller firms have been snapped up by bigger groups.

Many residences are clustered in deprived areas such as parts of northern England, where property is cheaper. Some 22% of England’s children’s homes places are in the northwest, the latest figures show. Just 8% are in London.

“The location of those properties is being driven by business considerations, rather than what’s in the interest of those children,” says Katharine Sacks-Jones, chief executive of Become, a charity for youngsters in care.

The Blackpool home Barnett was sent to was operated by Cambian Group, a specialist in this type of residential care. Cambian is part of the CareTech family of businesses, Britain’s largest operator of children’s homes.


In a statement to Bloomberg, CareTech says it “hasn’t purposely opened homes in areas where property is cheaper, but acquired the homes through the purchase of companies where the local founders have set up their businesses to meet local demands for children’s care services.”

It adds that in the past 10 years it “has only opened ‘new’ operational groups of services (where services did not previously exist) in Bedfordshire, Yorkshire, Newmarket, Hertfordshire and Bristol,” locations mainly in the wealthier south and southwest England.

Founded by entrepreneur brothers Farouq and Haroon Sheikh, CareTech was listed on London’s AIM exchange in 2005. With an initial value a touch above £60 million, it expanded through acquisitions and was taken private in a £1.2 billion deal in 2022 by the brothers and PE firm Three Hills Capital Partners.

As with many take-private deals, it was financed partly through debt. In this case, Ares provided three different loans with a total value of £760 million, according to offer documents. While the terms weren’t disclosed, such facilities are often secured on company assets and carry a yield of between 500 and 600 basis points over benchmark interest rates. Today, that would suggest a yield above 10%. CareTech and Ares declined to comment on the loans.


CareTech also used a popular PE technique to bring in more cash after going private. It sold its property portfolio of special schools, children’s homes and adult specialist care homes and rented them back, in what’s known as a sale-and-leaseback. The buyer was Civitas Investment Management, an advisory firm backed by billionaire Li Ka-shing’s CK Asset Holdings.

Aspris, the third-biggest owner of UK children’s homes, is controlled by Dutch private equity firm Waterland. The buyout group snapped up the business as part of a £1.1 billion deal in 2021 to buy The Priory Group. Aspris’ financing costs jumped by a third in the year to August 2023 as interest rates soared, according to filings.

An Aspris spokesperson says its funding model, including debt, is “tried and tested” and has let it “significantly invest in our provision delivering the outcomes these children rightly deserve.”

For critics, however, private capital’s motives are unlikely to ever fully align with the needs of young people in their ward. “We have decision making that’s about meeting debt requirements and managing the profits of shareholders,” John Pearce, corporate director of children and young people’s services at Durham County Council, told a parliamentary evidence session.


Going Local

More than half of Britain’s largest children’s home operators are private equity-owned, according to a Bloomberg analysis of data and filings from Ofsted and government register Companies House. This includes the three biggest operators — CareTech, Keys Group and Aspris — who owned 397 homes and housed 1,394 children between them at the end of March, the data shows. The price per child can reach up to £359,000 a year, although these can be youngsters with very complex needs requiring around-the-clock care.

Eyewatering costs, and a lack of suitable places, have prompted some local authorities to try to stem the privatization flow.

West Northamptonshire Council hopes to save cash by opening its own children’s accommodation. It says a council-owned place could save up to £70,000 per child yearly. It’s a promise that’s gaining political attention.

“To put children’s social care back on a sustainable footing, we need to put power back in the hands of local councils, so they can provide care services themselves,” says Munira Wilson MP, the Liberal Democrat education spokesperson. “Taking children away from their communities and support networks can really harm outcomes for those young people. The government's crackdown on private profiteering needs to deliver, urgently.”


As part of Phillipson’s plan, the government wants to encourage non-profit operators and is handing new powers to Ofsted to punish private underperformers and increase transparency around their finances. This includes taking action against placement providers who deliver subpar care and giving Ofsted the ability to to issue civil fines.

“If these measures don’t put an to end to profiteering, we won’t hesitate to cap profits,” a Department for Education spokesperson says.

Some experts are dubious, though, about whether politicians or regulators like Ofsted have the knowhow to properly police private-capital firms. Ludovic Phalippou, professor of financial economics at Oxford University’s Said Business School, says if the government tries to limit their profitability, large providers can find ways to show artificially lower margins.

In fairness to private operators, the Children’s Services Development Group supports the need for a combined effort between the independent providers it represents and their non-profit peers, to try to make up for years of austerity. “If we’re to address the challenges that the sector faces,” its chair Isaac says, “then a mixed-market economy, united by common goals and a determination to put children and young people first, is the best outcome.”


When things do go wrong, the result can be wretched. One young person, who asked to remain anonymous, says in one privately run home there were wasp nests. In another, there were maggots under a cupboard.

“While there are some brilliant people working in children’s homes, at the end of the day, profit-making companies are there to serve the interests of their owners,” says Sacks-Jones. “It’s a real concern when that starts impacting on the experiences of children.”

Most Read from Bloomberg Businessweek

‘It’s Hell for the Fish’: The US Has a Billion-Dollar Plan to Halt a Carp Invasion

The Coming Wave of New Obesity-Treatment Drugs

Biden Made This Billionaire Much Richer. The Bonanza Could End With Trump

Market-Moving Data Under Threat as Trump Returns to Washington

In a MedSpa, Your Surgeon May Be a Nurse"""
    #print(trans_summ_data(data))