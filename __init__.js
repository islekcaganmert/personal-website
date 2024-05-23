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
        let selectedTab = buttons[i].id.split('_')[0];
        document.getElementById(selectedTab + '_feed').style.visibility = 'hidden';
        document.getElementById(selectedTab + '_feed').style.height = '1px';
    }

    document.getElementById(tabId + '_feed').style.visibility = 'unset';
    document.getElementById(tabId + '_feed').style.height = 'max-content';
    let element = document.getElementById(tabId + '_button');
    element.style.color = color;
}

chooseTab('posts');
