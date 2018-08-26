"""Main entry point to run."""
# pylint: disable=no-value-for-parameter
import click

from jefit.decrypt import JefitDecryptor


@click.command()
@click.option("--filepath", help="The file to be decrypted.")
def main(filepath):
    """Main entry point."""
    try:
        decryptor = JefitDecryptor(filepath)
        decryptor.decrypt()
    except Exception as exception:
        raise exception


if __name__ == "__main__":
    main()
