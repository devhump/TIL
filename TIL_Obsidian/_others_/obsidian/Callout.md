#Obsidian 

### Callout
🔼 [[markdown for Obsidian]]

- Obsidian Specify grammer like 'adomition', or 'alert'

> [!NOTE]
> For compatibility reasons, 

```markdown
> [!INFO]
> Here's a callout block.
> It supports **markdown** and [[Internal link|wikilinks]].
```

> [!INFO]
> Here's a callout block.
> It supports **markdown** and [[Internal link|wikilinks]].


##### types
|     | type     | simillar           |
| --- | -------- | ------------------ |
|  1   | note     |                    |
|  2   | tdlr     | abstract, summary  |
|  3   | info     | todo               |
|  4   | tip      | hint, important    |
|  5   | check    | success, done      |
|  6   | question | help, faq          |
|  7   | caution  | warning, attention |
|  8   | fail     | failure, missing   |
|  9   | danger   | error              |
|  10   | bug      |                    |
|  11   | example  |                    |
|  12   | quote    | cite               |
 
>[!note]
>type example (1)

>[!tldr]
>type example (2)
>abstract, summary, tldr

>[!info]
>type example (3)
>info, todo

>[!tip]
>type example (4)
>tip, hint, important

>[!check]
>type example (5)
>check, success, done

>[!help]
>type example (6)
>help, question, faq

>[!caution]
>type example (7)
>warning, caution, attention

>[!fail]
>type example (8)
>failure, fail, missing

>[!error]
>type example (9)
>danger, error

>[!bug]
>type example (10)

>[!example]
>type example (11)

>[!quote]
>type example (12)
>quote, cite


### specific usage
```markdown
>[!note] 1. 한 줄로도 작성이 가능하다

>[!faq]- 2. 접을 수 있냐고?
>당연하지!

>[!bug]+ 3. 기본적으로 펴지게 설정도 가능
>이렇게!

> [!quote: 4. This is the title!] 
> This is an admonition!
```

>[!note] 1. 한 줄로도 작성이 가능하다

>[!faq]- 2. 접을 수 있냐고?
>당연하지!

>[!bug]+ 3. 기본적으로 펴지게 설정도 가능
>이렇게!


> [!quote: 4. This is the title!] 
> This is an admonition!


### Admonition
```ad-note # Admonition type. See below for a list of available types. 
title: 문제. 
icon: triforce 
collapse: open
color: 200, 200, 200

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. 
```

````
```ad-note # Admonition type. See below for a list of available types. 
title: 문제. 
icon: triforce 
collapse: open
color: 200, 200, 200

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla. 
```
````
