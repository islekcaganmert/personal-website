function chooseTab(tabId)
{
    let computedStyle = getComputedStyle(
        document.getElementsByClassName('button mini')[0]
    );
    let color = computedStyle.backgroundColor;
    computedStyle = getComputedStyle(
        document.getElementsByTagName('h1')[0]
    );
    let noColor = computedStyle.color;

    let buttons = document.getElementsByClassName('tab_button');
    for (let i in [0, 1, 2])
    {
        buttons[i].style.color = noColor;
    }

    let element = document.getElementById(tabId + '_button');
    element.style.color = color;
}

chooseTab('posts');