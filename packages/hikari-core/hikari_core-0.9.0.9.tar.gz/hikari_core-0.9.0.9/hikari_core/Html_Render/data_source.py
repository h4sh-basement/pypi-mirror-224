from os import getcwd
from pathlib import Path
from typing import Literal, Union

import aiofiles
import jinja2

from .browser import get_new_page

TEMPLATES_PATH = str(Path(__file__).parent / 'templates')

env = jinja2.Environment(
    extensions=['jinja2.ext.loopcontrols'],
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    enable_async=True,
)


async def text_to_pic(
    text: str,
    css_path: str = '',
    width: int = 500,
    type: Literal['jpeg', 'png'] = 'png',
    quality: Union[int, None] = None,
) -> bytes:
    """多行文本转图片

    Args:
        text (str): 纯文本, 可多行
        css_path (str, optional): css文件
        width (int, optional): 图片宽度，默认为 500
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效

    Returns:
        bytes: 图片, 可直接发送
    """
    template = env.get_template('text.html')

    return await html_to_pic(
        template_path=f'file://{css_path if css_path else TEMPLATES_PATH}',
        html=await template.render_async(
            text=text,
            css=await read_file(css_path) if css_path else await read_tpl('text.css'),
        ),
        viewport={'width': width, 'height': 10},
        type=type,
        quality=quality,
    )


# async def read_md(md_path: str) -> str:
#     async with aiofiles.open(str(Path(md_path).resolve()), mode="r") as f:
#         md = await f.read()
#     return markdown.markdown(md)


async def read_file(path: str) -> str:
    async with aiofiles.open(path, mode='r') as f:
        return await f.read()


async def read_tpl(path: str) -> str:
    return await read_file(f'{TEMPLATES_PATH}/{path}')


async def template_to_html(
    template_path: str,
    template_name: str,
    **kwargs,
) -> str:
    """使用jinja2模板引擎通过html生成图片

    Args:
        template_path (str): 模板路径
        template_name (str): 模板名
        **kwargs: 模板内容

    Returns:
        str: html
    """

    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_path),
        enable_async=True,
    )
    template = template_env.get_template(template_name)

    return await template.render_async(**kwargs)


async def html_to_pic(  # noqa: PLR0913
    html: str,
    wait: int = 0,
    template_path: str = f'file://{getcwd()}',  # noqa: B008
    type: Literal['jpeg', 'png'] = 'png',
    quality: Union[int, None] = None,
    use_browser: str = 'chromium',
    **kwargs,
) -> bytes:
    """html转图片

    Args:
        html (str): html文本
        wait (int, optional): 等待时间. Defaults to 0.
        template_path (str, optional): 模板路径 如 "file:///path/to/template/"
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效
        **kwargs: 传入 page 的参数

    Returns:
        bytes: 图片, 可直接发送
    """
    # logger.debug(f"html:\n{html}")
    if 'file:' not in template_path:
        raise Exception('template_path 应该为 file:///path/to/template')
    async with get_new_page(use_browser, **kwargs) as page:
        await page.goto(template_path)
        await page.set_content(html, wait_until='networkidle')
        await page.wait_for_timeout(wait)
        img_raw = await page.screenshot(
            full_page=True,
            type=type,
            quality=quality,
        )
    return img_raw


async def template_to_pic(  # noqa: PLR0913
    template_path: str,
    template_name: str,
    templates: dict,
    pages: dict = {  # noqa: B006
        'viewport': {'width': 500, 'height': 10},
        'base_url': f'file://{getcwd()}',  # noqa: B008
    },
    wait: int = 0,
    type: Literal['jpeg', 'png'] = 'png',
    quality: Union[int, None] = None,
) -> bytes:
    """使用jinja2模板引擎通过html生成图片

    Args:
        template_path (str): 模板路径
        template_name (str): 模板名
        templates (dict): 模板内参数 如: {"name": "abc"}
        pages (dict): 网页参数 Defaults to
            {"base_url": f"file://{getcwd()}", "viewport": {"width": 500, "height": 10}}
        wait (int, optional): 网页载入等待时间. Defaults to 0.
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效

    Returns:
        bytes: 图片 可直接发送
    """

    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_path),
        enable_async=True,
    )
    template = template_env.get_template(template_name)

    return await html_to_pic(
        template_path=f'file://{template_path}',
        html=await template.render_async(**templates),
        wait=wait,
        type=type,
        quality=quality,
        **pages,
    )


async def capture_element(
    url: str,
    element: str,
    timeout: float = 0,
    type: Literal['jpeg', 'png'] = 'png',
    quality: Union[int, None] = None,
    **kwargs,
) -> bytes:
    async with get_new_page(**kwargs) as page:
        await page.goto(url, timeout=timeout)
        img_raw = await page.locator(element).screenshot(
            type=type,
            quality=quality,
        )
    return img_raw
