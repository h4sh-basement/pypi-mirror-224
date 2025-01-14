import datetime
from tenji.model.user.profile import About, Profile
from tenji.parser.parser_base import ParserBase


class ProfileParser(ParserBase):
    def parse(self) -> Profile:
        username = self._soup.select_one("span.h1-headline-value > span.headline").text

        subtitle = self.try_get_text("span.h1-headline-value > span.subtitle")
        status = self.try_get_text("span.tbx-target-STATUS")

        # get background from style
        banner = self.try_get_style_background(
            self._soup.select_one("div.the-banner").get("style")
        )

        avatar = self._soup.select_one("img.the-avatar").get("src")
        stats_container = self._soup.select_one("div.object-stats")
        last_visit_node = stats_container.select_one("span:nth-child(1)")
        last_visit_relative = last_visit_node.text
        last_visit = self.try_parse_mfc_time(last_visit_node.get("title"), datetime.datetime.utcnow())
        joined_node = stats_container.select_one("span:nth-child(2)")
        joined_relative = joined_node.text
        joined = self.try_parse_mfc_time(joined_node.get("title"))

        eye_icon_node = stats_container.select_one("span.icon-eye")
        hits = self.try_extract_number(eye_icon_node.next_sibling)
        placement = self.try_extract_number(stats_container.select_one("small").text)

        about_container = self._soup.select_one("div.data_2")

        level = self.try_get_text(
            "div.form-label:-soup-contains('Level') + div > a", about_container
        )
        gender = self.try_get_text(
            "div.form-label:-soup-contains('Gender') + div > a", about_container
        )
        age = self.try_get_text(
            "div.form-label:-soup-contains('Age') + div", about_container
        )
        location = self.try_get_text(
            "div.form-label:-soup-contains('Location') + div", about_container
        )
        occupation = self.try_get_text(
            "div.form-label:-soup-contains('Occupation') + div", about_container
        )
        homepage = self.try_get_value(
            "div.form-label:-soup-contains('Homepage') + div > a", "href", about_container
        )
        shows = self.try_get_text(
            "div.form-label:-soup-contains('Shows(s)') + div > a", about_container
        )
        books = self.try_get_text(
            "div.form-label:-soup-contains('Book(s)') + div", about_container
        )
        games = self.try_get_text(
            "div.form-label:-soup-contains('Game(s)') + div", about_container
        )
        games = self.try_get_text(
            "div.form-label:-soup-contains('Game(s)') + div", about_container
        )
        moe_points = self.try_get_text(
            "div.form-label:-soup-contains('MOE Point(s)') + div", about_container
        )

        about = About(
            level=level,
            gender=gender,
            age=age,
            location=location,
            occupation=occupation,
            homepage=homepage,
            shows=shows,
            books=books,
            games=games,
            moe_points=moe_points,
        )

        return Profile(
            username=username,
            subtitle=subtitle,
            status=status,
            banner=banner,
            avatar=avatar,
            last_visit=last_visit,
            joined=joined,
            hits=hits,
            placement=placement,
            about=about,
        )
